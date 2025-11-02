from PIL import Image

def extract_watermark(image_with_watermark_path, output_path, watermark_size):
    """
    从图片中提取隐藏的水印。

    :param image_with_watermark_path: 带有隐藏水印的图片路径
    :param output_path: 提取出的水印图片的保存路径
    :param watermark_size: 原始水印的尺寸 (宽度, 高度)，必须提供
    """
    try:
        # 打开带有水印的图片
        img = Image.open(image_with_watermark_path).convert("RGB")

        # 获取水印尺寸
        width, height = watermark_size

        # 创建一张新的空白图片，用于绘制提取出的水印
        extracted_watermark = Image.new("1", (width, height))
        extracted_pixels = extracted_watermark.load()

        # 获取带水印图片的像素数据
        pixels = img.load()

        # 遍历指定的尺寸范围
        for x in range(width):
            for y in range(height):
                # 读取R通道的值
                r, _, _ = pixels[x, y]

                # 提取R通道的最低有效位 (LSB)
                # 如果r是偶数，最低位是0；如果是奇数，最低位是1
                lsb = r % 2

                # 根据最低有效位设置新图片的像素颜色
                # 0 -> 黑色, 1 -> 白色
                if lsb == 0:
                    extracted_pixels[x, y] = 0 # 黑色
                else:
                    extracted_pixels[x, y] = 255 # 白色

        # 保存提取出的水印图片
        extracted_watermark.save(output_path)
        print(f"水印提取成功！已保存至 {output_path}")

    except FileNotFoundError:
        print("错误：无法找到指定的图片文件。")
    except Exception as e:
        print(f"发生错误：{e}")

# --- 使用示例 ---
# 需要知道原始水印的尺寸才能正确提取
original_watermark_size = (512, 512) # 这里需要替换成真实水印图片的尺寸
extract_watermark('source_with_watermark.png', 'extracted_watermark.png', original_watermark_size)
