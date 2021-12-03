命令总结：
创建版本库
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱名"
git init

添加文件
git add .  (这是添加文件夹下所有的文件)
git add 单个或多个文件名称

提交文件
git commit -m "提交文件描述"

补充两个：
git log --oneline  # 可以查看已经提交后的操作对应的id
git status -s  # 查看文件当前状态

查看修改记录
git log

查看修改文件并提交后的状态，分为三类：
这里的操作只是用于对比修改前后有哪些不一样
git diff   # 查看没有add时候的状态，即unstaged状态
git diff --cached #查看已经add时候的状态，即staged状态
git diff HEAD #有没有add，都可以查看，即staged & unstaged状态都可以

修改操作，分这几种情况
git log --oneline 
git status -s  
情况一：修改后的文件已经commit了，发现还有个文件没有提交上去(这里说的是文件，情况有很多，比如：提交后下一秒又加了一行代码)，如果重新提交会有一次新的操作，怎么在刚刚提交的版本上把文件补上呢？
    git commit --amend --no-edit
情况二：如果只是对修改后的文件进行了add，发现还有个文件没有提交上去，如何退回到add之前的状态呢？
    git reset 当前文件名称
情况三：把修改后的文件已经add和commit操作了，如何返回上一个版本或者指定版本
    git reset --hard HEAD^  #回到上一个版本
    git reset --hard HEAD^^  #回到上上个版本
    ​
    git reset --hard HEAD~2  #回到上上个版本
    git reset --hard HEAD~100  #回到前100个版本

    git reset --hard XXXX  #XXXX表示commit对应版本的id号
情况四：现在退回到过去的版本了，发现过去版本更乱，如何回到未来的某个版本呢？
git reflog  #退回去之前某个版本之后，查看之后所有版本对应的id
    git reset --hard XXXX  # 想要返回的那个commit对应的id号

对单个文件进行操作--返回指定版本
    git checkout XXXX -- 文件名称  # 想要返回的那个commit对应的id号