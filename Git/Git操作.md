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

## 覆盖提交记录/撤销修改记录 8-1
- 覆盖提交记录
    - 在第一次提交之后，使用git commit --amend 命令 i 输入修改记录名称，也可以将未添加的文件写入文件中
    - wq! 退出
- 取消暂存文件
    - git reset HEAD <file>   针对已经 git add 的文件，撤销暂存的修改记录，变成未暂存之前的最初状态
- 撤销修改记录
    - git cheakout -- <file> 针对已经取消暂存的文件，撤销修改记录，变成未修改之前的状态

## 打标签（版本迭代/名称）
- 列出标签
    - git tag
- 存在多个子版本信息，例如 1.1.0 、 1.1.1,想要查询就可以进行该系列查询
    - git tag -l "v1.1.*"
- 附注标签
    - git tag -a v1.2 -m "my version 1.2"
- 轻量标签
    - git tag v1.4-lw
- 后期打标签 （记录提交之后的标签）
    - git log --pretty=oneline 查看历史版本 (uuid commit)
    - git tag -a v0.12 uuid[0:7] (获取前7位的ID值)
- 共享标签 （将本地标签提交到我们远程仓库中）
    - git push origin v1.5
- 删除标签 （将本地标签删除）
    - git tag -d v1.5
- 删除远程仓库标签 （将远程仓库标签删除）
    - git push origin :refs/tags/v1.5
- 检出标签
    - git checkout v1.5 (进入到当前标签版本中，去修改当前版本内容，即不更改后续版本信息)
    - 退出 git checkout master 切换到主分支

## 远程仓库的使用
- 创建远程仓库 在github上创建远程仓库信息，复制其链接 https://github.com/1581638690/tests.git
- git clone https://github.com/1581638690/tests.git 克隆这个仓库
- git remote 列出来当前所有的仓库别命
- git remote -v 列出来仓库的详细西信息
- git push origin master 将master分支中文件推送到 我们仓库origin中

- git remote add  tst1(别名) https://github.com/1581638690/tests1.git 新增远程仓库
- git fetch tst1 （获取远程仓库的版本信息，而我本地没有的版本信息）
- git remote rename tst1 test1 重命名仓库
- git remote remove test1 删除远程仓库