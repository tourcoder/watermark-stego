# Watermark Stego
隐藏水印（写入&提取）

### 使用

新建一个文件夹，比如 demo，将本仓库中的 embedding.py 和 extraction.py，以及用到的图片（source.png/watermark.png）放入到这个文件夹里，在终端里进入这个文件夹，然后执行下面的命令

```
python3 -m venv ./venv
source ./venv/bin/activate
```

激活虚拟环境，然后执行下面的命令安装模块

```
pip3 install Pillow
```

- 写入

  ```
  python3 embedding.py
  ```
  
- 提取

  ```
  phython3 extraction.py
  ```

Enjoy~
