[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16902766&assignment_repo_type=AssignmentRepo)
# MiniTorch Module 0

<img src="https://minitorch.github.io/minitorch.svg" width="50%">

* Docs: https://minitorch.github.io/

* Overview: https://minitorch.github.io/module0/module0/

## Task0_5: 
Here we notice that diag is separated from class 1 to class 0 by line x + y = 1, below this line is class 1, above - class 0. So this means our model should have negative dependencies (-1, -1) on x and y and have bias 0.5 (so at x = 0.5 it switches to predicting 0).
<img src="task0_5_params.png" width="50%">
<img src="task0_5_points.png" width="50%">