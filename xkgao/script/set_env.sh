#!/bin/bash

HOST="192.168.101.191"
PROXY_URL="http://$HOST:7890"
SOCKS_PROXY_URL="socks5://$HOST:7890"

# 设置代理
set_proxy() {
    export https_proxy=$PROXY_URL
    export http_proxy=$PROXY_URL
    export all_proxy=$SOCKS_PROXY_URL
    echo "Proxy has been set."
}

# 取消代理
unset_proxy() {
    unset https_proxy
    unset http_proxy
    unset all_proxy
    echo "Proxy has been unset."
}

# 判断参数
if [ "$1" == "set" ]; then
    set_proxy
elif [ "$1" == "unset" ]; then
    unset_proxy
else
    echo "Usage: $0 {set|unset}"
fi