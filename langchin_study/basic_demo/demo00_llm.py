import os
from PIL import Image


def create_id_photo(input_path, output_path, dpi=300):
    """
    将任意图片转换为一寸照 (25mm x 35mm, 300dpi)
    """
    if not os.path.exists(input_path):
        print(f"错误：找不到文件 {input_path}")
        return

    # 1. 一寸照的标准像素尺寸 (300 DPI 下)
    target_width = 295
    target_height = 413
    target_ratio = target_width / target_height  # 约 0.714 (5:7)

    try:
        # 打开原始图片，并转换为 RGB 模式（去除透明的 alpha 通道，防止存为 JPG 报错）
        img = Image.open(input_path).convert("RGB")
        orig_width, orig_height = img.size
        orig_ratio = orig_width / orig_height

        # 2. 智能居中裁剪 (Center Crop)
        # 如果原图比一寸照“宽”，则裁掉左右两边；如果比一寸照“长”，则裁掉上下两头
        if orig_ratio > target_ratio:
            # 原图太宽，以高度为准，裁剪左右
            new_width = int(orig_height * target_ratio)
            left = (orig_width - new_width) // 2
            top = 0
            right = left + new_width
            bottom = orig_height
        else:
            # 原图太长，以宽度为准，裁剪上下
            new_height = int(orig_width / target_ratio)
            left = 0
            top = (orig_height - new_height) // 2
            right = orig_width
            bottom = top + new_height

        # 执行裁剪
        img_cropped = img.crop((left, top, right, bottom))

        # 3. 等比例缩放到一寸照的标准像素大小
        # 使用 LANCZOS 算法保证缩放后的画质清晰
        img_resized = img_cropped.resize((target_width, target_height), Image.Resampling.LANCZOS)

        # 4. 添加 3mm 白边（防止照相馆打印裁剪时切到人脸）
        border_mm = 3
        border_px = int((border_mm / 25.4) * dpi)  # 毫米转像素，25.4mm = 1英寸

        final_width = target_width + border_px * 2
        final_height = target_height + border_px * 2

        # 创建纯白背景
        final_img = Image.new("RGB", (final_width, final_height), "white")
        # 将处理好的照片粘贴到中间
        final_img.paste(img_resized, (border_px, border_px))

        # 5. 保存图片，必须指定 dpi 为 300，否则打印出来尺寸不对
        final_img.save(output_path, dpi=(dpi, dpi), quality=95)
        print(f"✅ 成功！一寸照已保存至：{output_path}")
        print(f"📐 最终像素尺寸: {final_width} x {final_height} (含白边)")

    except Exception as e:
        print(f"❌ 处理失败: {e}")


if __name__ == "__main__":
    # 请将 "input.jpg" 换成你实际的图片路径
    input_image = "input.jpg"
    output_image = "output_1inch.jpg"

    create_id_photo(input_image, output_image)