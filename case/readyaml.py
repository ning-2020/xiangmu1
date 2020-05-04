import yaml
import os


def read_yaml(yamlPath):
    '''读取yaml文件
    文件真是的绝对路径'''
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确:%s" %yamlPath)
    #直接打开文件读取
    f = open(yamlPath,'r',encoding='utf-8')
    cfg = f.read()
    d = yaml.load(cfg,Loader=yaml.FullLoader)
    print("读取的测试文件数据：%s" %d)
    return d
if __name__ == '__main__':
    data = read_yaml("testdata.yaml")["updata_info"]
    print(data)
