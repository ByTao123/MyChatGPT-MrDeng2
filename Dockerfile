# python版本，可根据需求进行修改
FROM python:3.10.2-alpine

RUN mkdir /code

# 将代码和项目依赖添加到code文件夹
ADD ./ /code

# 设置code文件夹是工作目录
WORKDIR /code

RUN export PYTHONPATH=/usr/local/bin/python
RUN pip install -r requirements.txt

# 镜像运行时执行的命令，这里的配置等于 python main.py
ENTRYPOINT ["python","app.py"]