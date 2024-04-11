新工程上传：
# 执行命令前，必须先看#注释部分，再输入命令
1、第一步：安装 Git

2、初始化仓库
    #已经安装好jupyter，可以顺利运行的的情况下，在工程根目录地址栏输入：
    输入：jupyter lab
    打开 JupyterLab：file-new-terminal
    输入：git init
    #这将在当前目录下创建一个 .git 隐藏文件夹，用于存储版本控制信息。

3、添加文件到仓库
    输入：git add .
    #命令会添加当前目录下的所有文件添加到暂存区。
    #Git 在处理行尾序列时会根据要上传的文件进行判断。在不同的操作系统中，文本文件的行尾序列可能不同。Linux 和 macOS 系统使用 LF（Line Feed）作为行尾标记，而 Windows 系统通常使用 CRLF（Carriage Return Line Feed）。Git 会尝试在不同操作系统间移动文件时自动转换这些行尾序列，以避免潜在的兼容性问题。如果有警告信息表明，Git 将在下次接触到这些文件时将 LF 转换为 CRLF。这些警告通常不会阻止您提交或推送更改。出现警告信息可以不用管，继续下一步。

4、提交更改
    输入：git commit -m "Your commit message"
    #"Your commit message" 是提交时可以添加的注释信息，以方便了解这一次提交更改是什么内容，如果不添加信息，可以直接使用：
    输入：git commit

5、在github上新建一个仓库，请注意仓库的默认分支是main

6、与远程仓库同步
    输入：git remote add origin <repository-url>
    #将 <repository-url> 替换为远程仓库 URL，请使用该仓库的https地址，地址在code按钮下寻找。
    #如果想另外创建一个分支，<branch-name>是想设置的分支名称，可以使用以下命令：
    输入：git remote add <branch-name> <repository-url>

7、每次工程在本地编辑修改后，如果不改动分支，继续沿用此前的分支，只需要输入命令：
    输入：git add .     
        #请注意最后有个空格与.号。全部工程暂存，准备提交，不区分哪些修改哪些没改，虽然耗时但是安全。。
        ：git commit -m "Your new commit message"  
        # 替换Your new commit message为此次修改的原因，必须填写，否则无法push。
        ：git push
         
8、doccker操作： 
    #本机已经完成docker的安装，在工程目录下创建一个dockerfile文件（没有后缀名），内容如下：
    
    # 使用官方 Python 镜像作为基础镜像
    FROM python:3.11
    # 设置容器内的工作目录
    WORKDIR /app
    # 将当前目录下的所有文件复制到容器的工作目录中
    COPY . /app
    # 安装项目所需的依赖，包括 Jupyter Lab
    # 注意：如果你的项目有额外的依赖，请在这里添加或在 requirements.txt 文件中列出
    RUN pip install --no-cache-dir notebook jupyterlab
    # 当容器启动时运行 Jupyter Lab
    CMD ["jupyter", "lab", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
    
    
    输入：Digital-Image-Processing>docker build -t digital-image-processing .
    #创建一个关于digital-image-processing的镜像，请注意该语句最后有个空格与一个点。




