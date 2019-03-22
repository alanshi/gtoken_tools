### gtoken_tools用处:

用于快速获取跳板机密码+二次认证token组合生产的秘钥以便于登录服务器

### 使用方法

1. 在~/.gauth或任意文件里填写二次认证的secret信息(参照.gauth.example)
2. 在gtoken.py中填写跳板机密码和gauth的信息
3. 在需要获取登录token的时候运行 python gtoken.py，建议加到alias中