## 安装ubuntu
- ie浏览器-安装ubuntu

## ubuntu 网卡
- 选择桥接网卡
- cd /etc/netplan/
- sudo vim 当前路径下文件
```shell
network:
  version: 2
  ethernets:
    eth0:  # 确保这个网卡名称是正确的
      dhcp4: no
      addresses:
        - 192.168.1.10/24  # 确保每个地址前都有 `-`  # 确保跟宿主机一直地址段
      routes:
        - to: 0.0.0.0/0  # `to` 前面也需要 `-`
          via: 192.168.1.1             # 宿主机的网段
      nameservers:
        addresses:
          - 8.8.8.8  # 确保DNS地址也正确缩进，并有 `-`

```

## 解压/压缩tar文件
- sudo tar -xvf xx.tar.gz     ~解压文件
- sudo tar -czvf xx.tar.gz xx  ~压缩文件

## 解压/压缩gz文件
- sudo gzip filename
- sudo gunzip filename.gz

## sh执行权限
- sudo chmod +x xx.sh

## 从本地复制文件到远程主机
- scp /path/file username@remote_host:/path/file
## 从远程主机复制文件到本地
- scp username@remote_host:/path/file /path/file