set -x

function download_lvis_mini(){
    # 下载标注文件
    wget https://github.com/lvis-dataset/lvis-api/raw/master/data/lvis_v1_minival.json -O ../download/lvis-mini/lvis_v1_minival.json
}

# download_lvis_mini
git clone git@github.com:lvis-dataset/lvis-api.git