import os
import json
import argparse
from PIL import Image, ImageDraw, ImageFont
 
FONT_SIZE = 13*2
# IMAGE_FONT = ImageFont.truetype("arial.ttf", FONT_SIZE)
COLOR_LIST = ["red", "green", "blue", "cyan", "yellow", "purple",
              "deeppink", "ghostwhite", "darkcyan", "olive",
              "orange", "orangered", "darkgreen"]
 
 
class ShowResult(object):
    def __init__(self, args):
        self.args = args
        self.json_file_path = self.args.json_file_path
        self.img_path_root = self.args.img_path_root
        self.show_img_path_root = self.args.show_img_path_root
        # 构造id到category id到category name的映射
        self._category_id_convert_to_name()
        # 构造image id到image name的映射
        self._image_id_convert_to_name()
        self._data_preprocess()
 
    def _image_id_convert_to_name(self):
        self.image_id_name_dict = {}
        self.orig_image_id_name_dict = self.orig_json["images"]
        for idx, image_id_name_dict in enumerate(self.orig_image_id_name_dict):
            self.image_id_name_dict[image_id_name_dict["id"]] = image_id_name_dict["file_name"]
        print(f"dataset image 数目 {len(self.image_id_name_dict)}") # 4809

    def _category_id_convert_to_name(self):
        # 构建一个字典: {"category_id": category_name,...}
        orig_json_file = open(self.json_file_path, encoding='utf-8')
        self.orig_json = json.load(orig_json_file)
        print(f"dataset info:{self.orig_json['info']}")
        self.category_id_name_dict = {}
        orig_category_id_name_dict = self.orig_json["categories"]
        # 构建id和name的映射
        for idx, category_id_name_dict in enumerate(orig_category_id_name_dict):
            self.category_id_name_dict[category_id_name_dict["id"]] = category_id_name_dict["name"]
        print(f"dataset category 类别数 {len(self.category_id_name_dict)}") # 1203
 
    def _data_preprocess(self):
        # 构建一个字典: {"img_id": [{bbox_attr_dict}, ...], ...}
        result_json_file = open(self.json_file_path, encoding='utf-8')
        self.resut_json = json.load(result_json_file)
        self.resut_json = self.resut_json["annotations"]
        self.img_id_bboxes_attr_dict = {}
        for idx, result_ann in enumerate(self.resut_json):
            result_attr_dict = {"bbox": result_ann["bbox"],
                                #"score": result_ann["score"],
                                "category_id": result_ann["category_id"]}
            # 可能一个图片对应多个标注框
            if result_ann["image_id"] not in self.img_id_bboxes_attr_dict.keys():
                self.img_id_bboxes_attr_dict[result_ann["image_id"]] = []
                self.img_id_bboxes_attr_dict[result_ann["image_id"]].append(result_attr_dict)
            else:
                self.img_id_bboxes_attr_dict[result_ann["image_id"]].append(result_attr_dict)
        print(f"dataset image 数目 {len(self.img_id_bboxes_attr_dict)}") # 4752,有些图片没有标注

 
    def mainprocess(self):
        # 对 self.img_id_bboxes_attr_dict进行循环操作:
        # 对每一张图片
        for idx, (img_id, attr_dict_list) in enumerate(self.img_id_bboxes_attr_dict.items()):
            img_path = os.path.join(self.img_path_root, self.image_id_name_dict[img_id])
            print("当前正在处理第-{0}-张图片, 总共需要处理-{1}-张, 完成百分比:{2:.2%}".format(idx+1,
                                                                        len(self.img_id_bboxes_attr_dict.keys()),
                                                                        (idx+1) / len(self.img_id_bboxes_attr_dict.keys())))
            # 对每一个bbox标注
            img = Image.open(img_path, "r")  # img1.size返回的宽度和高度(像素表示)
            draw = ImageDraw.Draw(img)
            print(img_path)
            # 提取所有bboxes信息
            for jdx, attr_dict in enumerate(attr_dict_list):
                COLOR = COLOR_LIST[jdx % len(COLOR_LIST)]
                # 对每一个bboxes标注信息
                bbox = attr_dict["bbox"]
                #score = attr_dict["score"]
                category_name = self.category_id_name_dict[attr_dict["category_id"]]
                x1, y1 = bbox[0], bbox[1]
 
                top_left = (int(bbox[0]), int(bbox[1]))  # x1,y1
                top_right = (int(bbox[0])+int(bbox[2]), int(bbox[1]))  # x2,y1
                down_right = (int(bbox[0])+int(bbox[2]), int(bbox[1])+int(bbox[3]))  # x2,y2
                down_left = (int(bbox[0]), int(bbox[1])+int(bbox[3]))  # x1,y2
 
                draw.line([top_left, top_right, down_right, down_left, top_left], width=5, fill=COLOR)
 
                # 将类别和分数写在左上角
                #new_score = str(score).split('.')[0] + '.' + str(score).split('.')[1][:2]
                #draw.text((x1, y1 - FONT_SIZE), new_score, font=IMAGE_FONT, fill=COLOR)
                #draw.text((x1 + 25, y1 - FONT_SIZE), "|", font=IMAGE_FONT, fill=COLOR)
                draw.text((x1 , y1), str(category_name), fill=COLOR)
                print(f"category_name: {category_name}")

 
            # 存储图片
            save_path = os.path.join(self.show_img_path_root, self.image_id_name_dict[img_id])
            img.save(save_path)
            exit(-1)
 
 
def main():
    parser = argparse.ArgumentParser()
    # json文件路径
    parser.add_argument('-json_file_path', default="instances_val2017.json",
                        help='the single img json file path')
    # 图片文件夹root
    parser.add_argument('-img_path_root', default='coco/val2017',
                        help='the val img path root')
 
    # 显示图片存储文件路径
    parser.add_argument('-show_img_path_root', default='coco_val2017',
                        help='the show img path root')
 
    args = parser.parse_args()
    showresult = ShowResult(args)
 
    showresult.mainprocess()
 
 
if __name__ == '__main__':
    main()
