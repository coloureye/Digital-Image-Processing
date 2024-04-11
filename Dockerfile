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