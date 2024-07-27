# 2024/7/22版本控制Git
## Git三种状态
Git有三种状态，你的文件可能处于其中之一：已提交（committed）、已修改（modified）和已暂存（staged）。

## Git配置信息
- Ubuntu安装git
    sudo apt  install git
- 添加配置信息
git config --global user.name "Your Name"
git config --global user.email "email@example.com"

## 创建版本库
- 选择文件夹
 cd /opt/code
- 初始化文件夹
  - git init
  - echo "#hello world" >> README.md
  - git status
  - git add README.md
  - git commit -m "first File"

## 查看历史记录
- 查看历史版本
    - git log  查看所有历史
    - git log -p -2 查看前2条修改历史