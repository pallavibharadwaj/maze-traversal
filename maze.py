#!/usr/bin/python3
import urllib.request, json
import re

url = "https://challenge.maze.com/"

def start():
    # start traversing the maze
    start_url = url+"start"
    response = urllib.request.urlopen(start_url)
    return response

def maze_identifier(response):
    # extract s
    sep = re.compile(r'^https:\/\/challenge.maze.com\/step\?s=(\d+\.\d+)&x=0&y=0$')
    s = sep.split(response.geturl())[1]
    return s

def get_coordinates(prev_url):
    sep = re.compile(r'^https:\/\/challenge.maze.com\/step\?s=\d+\.\d+&x=(\d+)&y=(\d+)$')
    xy = sep.split(prev_url)[1:3]
    xy = {'x': int(xy[0]), 'y': int(xy[1])}
    return xy

def find_next(data, visited, prev_xy):
    for xy in data['adjacent']:
        if(len(data['adjacent'])==1):   # dead end
            return xy
        elif(xy not in visited):   # un-explored path
            return xy
    return data['previous']

def test_success(s, path):
    # check correctness of path
    test_url = url+"check"+"?s=%s&guess=%s" % (s, path)
    response = json.loads(urllib.request.urlopen(test_url).read())
    return response['success']

def step(s, next_xy):
    params = "s=%s&x=%s&y=%s" % (s, next_xy['x'], next_xy['y'])
    step_url = url+"step?"+params
    print(step_url)
    response = urllib.request.urlopen(step_url)     # goto adjacent node
    return response

def traverse(s, response):
    backtr_xy = {}
    url = response.geturl()

    # adjacent to first node 
    data = json.loads(response.read())
    path = data['letter']   # first node
    visited = [{'x': 0, 'y': 0}]

    # traverse until the end
    while(data['end'] != True):
        prev_xy = get_coordinates(url)
        url = response.geturl()

        # remember previous node to backtrack
        if(url not in backtr_xy):
            backtr_xy[url] = prev_xy 
        data['previous'] = backtr_xy[url] 

        next_xy = find_next(data, visited, prev_xy)     # find next step

        if(next_xy not in visited):
            visited.append(next_xy)

        response = step(s, next_xy)    # goto next coordinates
        data = json.loads(response.read())
        path = path + data['letter']

    return path

def main():
    response = start()
    s = maze_identifier(response)

    path = traverse(s, response)
    print("s = %s, path = %s" % (s, path))

    if(test_success(s, path)):
        print("Maze traversed Successfully")
    else:
        print("Maze traversal Unsuccessful")

if __name__=='__main__':
    main()
