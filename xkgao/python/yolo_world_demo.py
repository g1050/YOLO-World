from ultralytics import YOLOWorld, YOLO

def infer_all_category():
    model = YOLOWorld('download/yolov8s-worldv2.pt')
    results = model.predict('download/bus.jpg')
    # print(results[0])

def infer_single_category():

    # Initialize a YOLO-World model
    model = YOLO('download/yolov8s-worldv2.pt')  # or choose yolov8m/l-world.pt
    
    # Define custom classes
    model.set_classes(["person"])
    
    # Execute prediction for specified categories on an image
    results = model.predict('download/bus.jpg')
    
    # Show results
    results[0].show()

def main():
    # infer_all_category()
    infer_single_category()

if __name__ == '__main__':
    main()