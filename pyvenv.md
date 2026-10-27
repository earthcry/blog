Python虚拟环境。

venv

 创建虚拟环境
创建虚拟环境的基本语法如下：

python -m venv <环境名称>
例如，创建一个名为myproject的虚拟环境：

python -m venv myproject
激活虚拟环境

Linux/macOS系统
source myproject/bin/activate
激活成功后，命令行前会显示虚拟环境名称：

(myproject) $ 
退出虚拟环境
deactivate
删除虚拟环境
直接删除虚拟环境文件夹即可：
# Linux/macOS
rm -rf myproject

- [ ] 升级pip