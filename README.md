# LCWT

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

![git](https://user-images.githubusercontent.com/83813866/204014817-952b68d1-ed88-414f-9445-a50fafd283b7.png)


 * **Coding game** made in the form of **stage game** so that **children** who are new to **coding** can easily understand the principles of **algorithms**
 * You can easily edit or make stages of game

<br>

## Why LCWT

* It has **simple** and **intuitive** GUI so that very **young** students can also learn coding

<img width="712" alt="스크린샷 2022-12-09 오후 11 19 39" src="https://user-images.githubusercontent.com/83813866/206722596-cccdf4f5-341d-4b5c-8f25-c340c3096274.png">

<img width="712" alt="스크린샷 2022-12-10 오전 12 02 02" src="https://user-images.githubusercontent.com/83813866/206731246-27a5a343-64ed-4973-8992-66ca4ada43c7.png">

<img width="712" alt="스크린샷 2022-12-10 오전 10 58 36" src="https://user-images.githubusercontent.com/83813866/206823299-26ec455f-cf55-44ed-9bea-754ac1103df0.png">


* You can easily make **stages** of coding game of your own with just **sequence** of commands.
```python
stage = Stage("stage/")
stage.save_stage(1,["Forward()","Left()"],(50,0))
```

* **LCWT** is very **light** and uses **standard** librarys of python such as `tkinter` `time` `turtle` so there is no need to install additional librarys except for `pillow`

<br>

## How to use

* First clone LCWT codes
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

  * You can currently use `Forward`, `Left`, `Right`, `Put`and I will add more on next update
  * `Put` can be used only once.
  * Only commands that are used are automatically added as buttons in stage.

```python
path = "path to save stage"
stage = Stage(path)

instructList = ["Forward()","Forward()"]
goal = (100,0)

stage.save_stage(stage_idx,instructionList,goal)
```

* ... Or you can simply use games already made by running `main.py`
```python
python main.py
```

<br>

## Game rule

* The goal of the game is to move the turtle along a given path into the puddle. It is shown at the start of the game and can be checked again through the `Goal` button
* Users can add commands to the command list by clicking command buttons.
* `Run` button will execute a list of commands line by line and if you successfully moved the turtle, you can move on to the next stage.
* `Debug` button can be used to check commands one by one slowly.
* `Delete` button will remove a last command of command list.

<img width="400" alt="스크린샷 2022-12-10 오전 10 58 36" src="https://user-images.githubusercontent.com/83813866/206907002-cb46d4ec-1684-4cac-bc39-4e66e79a439e.gif">


<br>

## TODO
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
