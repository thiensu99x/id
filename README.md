<h1 align="center">Apple ID 自动化管理</h1>
<p align="center">
    <a href="https://github.com/pplulee/appleid_auto/issues" style="text-decoration:none">
        <img src="https://img.shields.io/github/issues/pplulee/appleid_auto.svg" alt="GitHub issues"/>
    </a>
    <a href="https://github.com/pplulee/appleid_auto/stargazers" style="text-decoration:none" >
        <img src="https://img.shields.io/github/stars/pplulee/appleid_auto.svg" alt="GitHub stars"/>
    </a>
    <a href="https://github.com/pplulee/appleid_auto/network" style="text-decoration:none" >
        <img src="https://img.shields.io/github/forks/pplulee/appleid_auto.svg" alt="GitHub forks"/>
    </a>
    <a href="https://github.com/pplulee/apple_auto/blob/main/LICENSE" style="text-decoration:none" >
        <img src="https://img.shields.io/github/license/pplulee/appleid_auto" alt="GitHub license"/>
    </a>
</p>
<h3 align="center">中文文档 | <a href="README_en.md">English</a> </h3>
<h3 align="center">请仔细阅读本文档以及使用说明，再使用。</h3>
<h3 align="center">使用本项目可能需要一定的基础知识。</h3>
<h3 align="center">本项目仍在更新当中。</h3>

# 基本简介

“以全新方式管理你的 Apple ID” —— 这是一款基于密保问题的自动化 Apple ID 检测&解锁程序。

前端用于管理账号，支持添加多个账号，并提供展示账号页面；

支持创建包含多个账号的分享页面，并可以为分享页面设置密码。

后端定时检测账号是否被锁定，若被锁定或开启二步验证则自动解锁，修改密码并向API回报密码。

登录Apple ID并自动删除Apple ID中的设备。

启用代理池和Selenium集群，提高解锁成功率，防止风控。

# 项目特点

- 多用户使用，权限控制
- 多账号管理
- 账号分享页，支持设置密码、有效期、自定义HTML内容
- 自动解锁与关闭二步验证
- 自动/定时修改密码
- 自动删除Apple ID中的设备
- 代理池与Selenium集群，提高解锁成功率
- 允许手动触发解锁
- ……

# 使用文档

我们已将所有文档与使用说明整理到了GitBook上，欢迎前往查看：

https://appleid-auto.gitbook.io/doc_zhcn/

# 问题反馈&交流

开发者水平和能力有限，程序可能存在诸多bug，欢迎提出 Issue 或 Pull Request ，也欢迎各位大佬加入项目，贡献代码！ \
Telegram群：[@appleunblocker](https://t.me/appleunblocker)

---

# 请我喝杯可乐

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/baiyimiao) \
USDT-TRC20: TV1su1RnQny27YEF9WG4DbC8AAz3udt6d4 \
ETH-ERC20：0xea8fbe1559b1eb4b526c3bb69285203969b774c5 \
其余赞助方式欢迎联系开发者
# Go to the root directory of the website and execute the following commands:

```
wget https://getcomposer.org/installer -O composer.phar
php composer.phar
php composer.phar install
```
# Set the website's running directory to /public and configure the pseudo-static-page setting to:
```
location ~* (runtime|application)/{
    return 403;
}
location / {
    if (!-e $request_filename){
        rewrite  ^(.*)$  /index.php?s=$1  last;   break;
    }
}
```
# Execute the following command in the website's root directory to create an administrator account:
```
php think register <username> <password>
```
