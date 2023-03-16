# Dian团队春招AI算法学习记录

```
胥皓元 自卓2201

U202215211

1318383762@qq.com
```

## Level 0

***一、Git与Github的使用***

**理论知识**

1. 配置信息

使用 git config --list 查看配置信息

2. 工作原理

如下为Git工作流程：

![Git 原理图](https://www.runoob.com/wp-content/uploads/2015/02/git-process.png)

如下图为Git工作区、缓存区、版本库：

![Git 原理图](https://www.runoob.com/wp-content/uploads/2015/02/git-command.jpg)

- 工作区：就是你在电脑里能看到的目录。

- 暂存区：英文叫 stage 或 index。一般存放在 .git 目录下的 index 文件（.git/index）中，所以我们把暂存区有时也叫作索引（index）。

- 版本库：工作区有一个隐藏目录 .git，这个不算工作区，而是 Git 的版本库。

**操作方式**

- 本地仓库及相关处理

在选定准备作为工作区的文件夹下右键，选择 git bash here ，再打开进入bush界面，进行 git init 初始化一个仓库（dian），在仓库中创建文件夹（mypro）放入文件用以提交。

*选择git bash here 相当于打开某个本地仓库分支（？），所以在工作中断以后想直接在git中对某个文件夹内进行处理可用以上操作。*


*工作区中的隐藏目录.git才是版本库，而未隐藏的工作文件夹（此处以我使用的mypro文件夹为例）不是，所以把文件移动到mypro中或在其中进行保存，并没有传入版本库，不能直接 git push*

然后利用

```
git add 文件名
git add 文件夹名/
```

将文件或文件夹添加到暂存区，再用

```
git commit -m [备注信息] 文件名
git commit -m [备注信息] 文件夹名/
```

将暂存区的文件或文件夹添加到版本库。

- 远程仓库及相关处理

*此处以GitHub为例*

sign up并sign in GitHub，创建一个repository，//

//***注意尽量不要勾选“使用README.md文件初始化仓库”，因为这样会进行一次初始提交，仓库就有了README.md和.gitignore文件，然后我们把本地项目关联到这个仓库，并把项目推送到仓库时，我们在关联本地与远程时，两端都是有内容的，但是这两份内容并没有联系，当我们推送到远程或者从远程拉取内容时，都会有没有被跟踪的内容，于是你看git报的详细错误中总是会让你先拉取再推送，但是拉取总是失败。***

错误情况如下：

![Git 报错](https://img-blog.csdnimg.cn/20200522092950149.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1ODkzOTk5,size_16,color_FFFFFF,t_70)

解决办法：

- 对于error: failed to push some refsto‘远程仓库地址’

先使用如下命令

```
git pull --rebase origin master
```

然后再上传

```
git push -u origin master
```

- 或者在创建远程仓库的时候就保持一个空仓库，什么也不要勾选❌//

//回到原文，远程仓库建好以后，在git中使用

```
git remote add 别名 远程仓库地址
```

别名可以未后续上传操作更便捷，即使md不能用鼠标移动光标，但可右键paste或直接ctrl+V.

利用

```
git remote -v
```

检查别名。

- 上传至远程仓库

首先确保文件已存入本地仓库中，用

```
git push [远程仓库地址/别名] [本地仓库分支]
```

以将本地仓库的文件上传到远程仓库的同名分支。

- 从远程仓库拉取

```
git clone
```

拷贝一份远程仓库（即全部下载）

- 分支

```
git branch  //查看已有分支
git branch 分支名   //创建新分支
git checkout 分支名   //切换到该分支下
git checkout -b 分支名   //创建新分支并立即切换到其下
```

***二、（小插曲）Markdown的使用***

这是第一天晚上在和一个同学探讨时发现的，此前一直想找到一个文本编辑器，现在发现了一个功能如此强大的编辑器，那就不得不冲了。
直接上演示吧，

————————

# Markdown 
## About how to use markdown

正文直接输入即可

正文换行要空一行
否则会被认为未换行

```
int main()
{
    printf("Hello, world!");
}
```

```python
print {
    "Hello, world."
}
```

有序列表
1. 123
2. 456
3. 789
    1. 123
    2. 234
        1. 123
        2. 234

无序列表
- 123
- 345
- 456
    - 123
    - 234

**加粗**

*倾斜*

***加粗与倾斜***

## Markdown图片

```
![alt 属性文本](图片地址)
```

可显示网上的图片，但不能设置长、宽。

*演示完毕*

————————

***三、机器学习部分重要概念***

1. 数据集

    1. 什么是数据集?
由数据样本组成的集合。
样本之间是独立的（不依赖其他样本），单个样本拿出来仍然可以称为此目标的样本。（最好）没有必然联系（除目标外），比如飞机和蓝天，如果数据集中的飞机都出现在蓝天里，结果可能将蓝天也分类为飞机，或其他背景中的飞机不会被识别。
    
    2. 什么样的数据集是好的？样本数量足够多,分布比较广（尽可能包含目标物体所有情况）

    3. 怎样划分数据集？
我们获得数据后要对其进行划分，数据集一般包括：

        训练集（Training Set）：模型用于训练和调整模型参数。

        验证集（Validation Set）：用来验证模型精度和调整模型超参数，选择模型。

        测试集（Test Set）：测试模型的泛化能力，最终对模型评估。

        因为训练集和验证集是分开的，所以模型在验证集上面的精度在一定程度上可以反映模型的泛化能力。在划分验证集的时候，需要注意验证集的分布应该与测试集尽量保持一致，不然模型在验证集上的精度就失去了指导意义。
在使用数据集训练模型之前，我们需要先将整个数据集分为训练集、验证集、测试集。训练集是用来训练模型的，通过尝试不同的方法和思路使用训练集来训练不同的模型，再通过验证集使用交叉验证来挑选最优的模型，通过不断的迭代来改善模型在验证集上的性能，最后再通过测试集来评估模型的性能。如果数据集划分的好，可以提高模型的应用速度。如果划分的不好则会大大影响模型的应用的部署，甚至可能会使得我们之后所做的工作功亏一篑。

## Level 1

**环境配置**

主要谈谈自己在配置环境时遇到的问题及解决方法：

1. pandas和numpy都是功能强大的python数据分析处理库，（所以我认为）仅需下载其中之一即可。
2. 安装pytorch和cuda较麻烦（其实也不是太麻烦，但我莫名卡了一天时间）：
    1. 对于torch库，先下载数据科学项目管理器anaconda，打开anaconda powershell prompt，打开pytorch官网下载界面，copy下方的一句命令，在命令行中paste即开始下载，*与网上的教程不同，现在下载pytorch好像都能下载，并不存在无法获取部分镜像资源包的情况*，***这里就卡了一会，因为几乎所有教程都在使用清华的镜像资源网站下载pytorch和torchvision***。
    2. 对于cuda，按教程来就好了，但因为一开始安装cuda前我运行cnn1.py程序，发生了报错：
   ```
   Error loading "C:\ProgramData\Anaconda3\lib\site-packages\torch\lib\caffe2_nvrtc.dll" or one of its dependencies.
   ```

   ![python 报错](https://img-blog.csdnimg.cn/img_convert/d726a16fb313c905e2e02fe106a4f964.png)

    CSDN上的说法有“pytorch版本问题，原来安装的是GPU版本，改为CPU版本后正常，conda install pytorch torchvision cpuonly -c pytorch”，然后我以为是没下载cuda导致的，但当时忘记了下载的是CPU版本的torch还是GPU版本的（（（

    *还有一个小插曲：当时我发现缺失的是.dll文件，网上查询后我从git上扒了个dependencies插件，用于检测是否缺失.exe文件或.dll文件运行时所必须的文件，但研究了一番后发现不会用。。。*

    于是下载CUDA后，我再次在VScode打开cnn1.py，发现还是报错，比较发现我的解释器选择好像有错。在VScode中甚至找不到python3.9.13('base')这一解释器，于是我打开Pycharm，在其中（强行）添加解释器。在pycharm中run了一遍，成功了。后来在VScode中run，发现也成功了，再看解释器，也变成了正确的解释器（这里不知道为什么是同步修改的）。所以我初步认为报错就是因为之前解释器选择错误。

    **测试结果**
    
![测试结果1](G:\大学资料\微信截图\测试结果1.png "测试结果1")

![测试结果2](G:\大学资料\微信截图\测试结果2.png )

# Level 2