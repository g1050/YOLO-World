
# pushd download/yolov5/yolov5/val.py
python download/yolov5/yolov5/val.py --weights /data/xkgao/YOLO-World/xkgao/download/yolov5/yolov5s.pt \
    --data /data/xkgao/YOLO-World/xkgao/download/yolo/convert/data.yaml \
    --img 640 --task test \
    --workers 2
# popd