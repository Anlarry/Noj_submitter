<font size = 6>Noj_submitter</font>
-------
<h2>Version 1.2</h2>
<font size = 3>
what's new
<ul>
    <li> 在noj_submitter中查看错误详情</li>
</ul>   
</font>

<h2>Version 1.1</h2>
<font size = 3>
<ul>
    <li> 提交noj.cn当前的考试中的题目<br/>
    </li>
    <li>查看AC过的题目的代码  <br/>
    </li>
</ul>

[demo_1](https://github.com/Anlarry/Noj_submitter/blob/master/Noj_submitter_v1.1/demo/cur_contest_demo.mht)  
[demo_2](https://github.com/Anlarry/Noj_submitter/blob/master/Noj_submitter_v1.1/demo/view_src_demo.mht)

因为使用了IEwebdriver，所以要检查IE浏览器的配置：
<ul>
    <li> IE页面的显示比例要为100%  </li>
    <li>IE选项设置的安全页中，4个区域的启用保护模式的勾选都去掉（或都勾上）</li>
    <li>IE浏览器为兼容模式</li>
</ul>
</font>  

---------
<h2>Introduce</h2>
<font size = 3>
&nbsp;&nbsp;&nbsp; Noj_submitter is a submiiter for noj.cn.  

<img src = "https://raw.githubusercontent.com/Anlarry/Noj_submitter/master/RealseNote/over_view.png" width="438" height = "345"></img>

你可以通过Noj_submitter向noj.cn提交代码，或者查看题目。
</font>

<h2>Usage</h2>
<font size = 3>
&nbsp;&nbsp;&nbsp; 输入相关信息->选择语言->提交代码

参数信息：  
<ul>
    <li>problem: ID of the problem  </li>
    <li>file: 文件路径</li>
</ul>
&nbsp;&nbsp;&nbsp; Warning: 因为submitter可能不会检查填入信息的正确性，因此你需要确保输入正确的参数

Run .exe in dict  
<img src = "https://github.com/Anlarry/Noj_submitter/blob/master/RealseNote/demo.gif" width="438" height = "345"></img>
<!-- <iframe height=438 width=345 src="demo.mp4"></iframe> -->

</font>

<h2>About txt/gif file</h2>
<font size = 3>
<ul>
    <li>language.txtr: 存储提交的语言, 1->C++, 3->G++</li>
    <li>num_to_show_model.txt: 打开Algorithm后显示的数量</li>
    <li>password.txt: 记录用户信息</li>
    <li>out_time.txt: 响应超时时间，因为noj.cn不稳定所以默认值设为10s</li>
    <li>img.gif: 封面图片, 可以用一个大小相同(700x200)的gif代替(文件名保持一致)</li>
</ul>
</font>
 
<h2>FAQ</h2>
<font size = 3>
<ul>
    <li>time out: 与noj.cn连接超时</li>
    <li>problem not find: 1.输入正确的题号; 2.noj.cn炸了</li>
</ul>
</font>


<h2>More</h2>
<font size = 3>
<ul>
<li>submitter通过post和get向noj.cn发送请求实现提交代码、查看测评信息</li>
<li>submitter'GUI is made by tkinter</li>
<li>当前的考试中提交代码通过selenium模拟,使用IEwebdriver</li>
<rl>
</font>

<h2>Download</h2>

[百度云](https://pan.baidu.com/s/1sDLWSIbt4vZRla0YlBROMg)
[version_1.2](https://github.com/Anlarry/Noj_submitter/blob/master/dist_v1.2.zip)
