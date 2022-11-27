# LCWT

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

![git](https://user-images.githubusercontent.com/83813866/204014817-952b68d1-ed88-414f-9445-a50fafd283b7.png)


 * **Coding game** made in the form of a **stage game** so that **children** who are new to coding can easily understand the principles of **algorithms**
 * You can easily edit or make stages of game

<br>

## Why LCWT

* It has **simple** and **intuitive** GUI so that very **young** students can also learn coding
<img width="712" alt="스크린샷 2022-11-26 오후 3 30 39" src="https://user-images.githubusercontent.com/83813866/204075573-8d068b5a-a2b1-4da4-8c6b-722f512e6247.png">


* You can easily make **stages** of coding game of your own with just **sequence** of turtle commands.
```python
stage = Stage("stage/")
stage.save_stage(1,["turtle.forward(50)","turtle.forward(50)"],(100,0))
```

* **LCWT** is very **light** and uses **standard** librarys of python such as `tkinter` `time` `turtle` so there is no need to install additional librarys except for `pillow`

<br>

## How to use

* First you have clone LCWT codes
```git
git clone https://github.com/qowngus33/learn_coding_with_turtle
```

* Install pillow
```
pip install pillow==9.3.0
```

* You can run LCWT game by following commands
```python
path = "path for getting stage information pickle files you created"
instructList, goal = Stage(path).stages()

app = LearnCodingWithTurtle(tk.Tk(),instructList, goal)
tk.mainloop()
```
* You can make and save stages by following commands
```python
path = "path for saving stage information pickle files you created"
stage = Stage(path)

instructList = ["turtle.forward(50)","turtle.forward(50)"]
goal = (100,0)

stage.save_stage(stage_idx,instructionList,goal)
```

* ... Or you can simply use games already made by running `main.py`
```python
python main.py
```

<br>

## TODO
* Add tutorials for learning button uses
* Add buttons for going forwards and backwards at game stage selecting page
* Add obstacle adding process in Stage class
* Add GUI for making games and auto saving of goals
* Add program logics such as for loop

<br>

## License
```
Copyright 2022 JuHyun Bae.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
