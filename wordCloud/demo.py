# coding:utf-8
from os import path
from jieba import lcut
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 读取去停用词库
def getStopWords():
    file = open('stopwordList/stopword.txt', 'r',encoding='utf8')
    words = [i.strip() for i in file.readlines()]
    file.close()
    return words

def generate_wordcloud(text,a):
    '''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
    d=path.dirname(__file__)
    font_path=path.join(d,"font//msyh.ttf")
    wc = WordCloud(background_color="white",# 设置背景颜色
           max_words=2000, # 词云显示的最大词数
           font_path=font_path, # 兼容中文字体，不然中文会显示乱码
                  )

    # 生成词云
    wc.generate(text)

    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, a))

    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")# 关掉图像的坐标
    plt.show()



if __name__=='__main__':

    # 读取文件
    d = path.dirname(__file__)
    text = open(path.join(d,'data//data.txt'),encoding='utf-8').read()
    # 分词
    words = lcut(text)
    # 去停用词
    stop_words = getStopWords()
    words = [i for i in words if not i in stop_words]
    word_string = ', '.join(words)
    # 生成词云
    generate_wordcloud(word_string,'wordcloud.png')
