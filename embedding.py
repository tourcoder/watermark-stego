from PIL import Image

def embed_watermark(carrier_path, watermark_path, output_path):
    """
    将水印图片嵌入到载体图片中。

    :param carrier_path: 载体图片的路径
    :param watermark_path: 水印图片的路径 (应为黑白二值图)
    :param output_path: 输出带水印的图片路径
    """
    try:
        # 打开载体图片和水印图片
        carrier_img = Image.open(carrier_path).convert("RGB")
        watermark_img = Image.open(watermark_path).convert("1") # 转换为二值图像 (1-bit pixels, black and white)

        # 检查水印图片尺寸是否小于或等于载体图片
        if watermark_img.width > carrier_img.width or watermark_img.height > carrier_img.height:
            raise ValueError("水印图片的尺寸不能大于载体图片")

        # 获取图片的像素数据
        carrier_pixels = carrier_img.load()
        watermark_pixels = watermark_img.load()

        # 遍历水印图片的每一个像素
        for x in range(watermark_img.width):
            for y in range(watermark_img.height):
                # 获取载体图片对应位置的像素RGB值
                r, g, b = carrier_pixels[x, y]

                # 获取水印图片对应位置的像素值 (0为黑色, 255为白色)
                # Pillow的"1"模式下，黑色是0，白色是255
                watermark_bit = 1 if watermark_pixels[x, y] == 255 else 0

                # 将水印信息写入载体图片R通道的最低有效位
                # bin(r)[:-1] 取出r的二进制表示（除了最后一位）
                # str(watermark_bit) 将水印的0或1转为字符串
                # 两者拼接后，用int(..., 2)转回十进制
                r_new = int(bin(r)[:-1] + str(watermark_bit), 2)

                # 将修改后的像素值写回
                carrier_pixels[x, y] = (r_new, g, b)

        # 保存带有隐藏水印的图片
        carrier_img.save(output_path, "PNG") # 建议保存为PNG无损格式
        print(f"水印嵌入成功！已保存至 {output_path}")

    except FileNotFoundError:
        print("错误：无法找到指定的图片文件。")
    except Exception as e:
        print(f"发生错误：{e}")

# --- 使用示例 ---
# 假设你有 source.png 和 watermark.png 在同一个文件夹下
embed_watermark('source.png', 'watermark.png', 'source_with_watermark.png')
