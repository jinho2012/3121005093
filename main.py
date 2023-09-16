import gensim
import jieba
import re
import sys

def info(msg):
    print("\033[32m[*]"+msg+" \033[0m")

def filter_str(str):
    self_re = re.compile(u"[^0-9A-Za-z\u4e00-\u9fa5]")
    string = self_re.sub("", str)
    result = jieba.lcut(str)
    return result

def read_file(path):
    with open(path, encoding='utf-8') as fd:
        data = fd.read()
        info("get "+path+" data sucess")
     
    return data


def check_main(origin, target):
    texts = [origin, target]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus,num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(origin)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim


def main():
    try:
        #origin_path = "C:/Users/jinghao/Desktop/work/ruangong/test/orig.txt"
        #target_path = "C:/Users/jinghao/Desktop/work/ruangong/test/orig_0.8_del.txt"
  
        #result_path = "C:/Users/jinghao/Desktop/work/ruangong/test/res.txt"
        origin_path = sys.argv[1]  # 论文原文的文件的绝对路径
        target_path = sys.argv[2]  # 抄袭版论文的文件的绝对路径
        result_path = sys.argv[3]  # 输出结果绝对路径
        origin_data = filter_str(read_file(origin_path))
        target_data = filter_str(read_file(target_path))
        check_result = check_main(origin_data , target_data)
        info("文章相似度： %.4f" % check_result)
        with open(result_path, 'w') as fd:
         fd.write("文章相似度： %.4f" % check_result)
         info("save result in "+result_path+"  sucess")
        result = round(check_result.item(), 2)  # 取小数点后两位
    except IOError:
        print("IO operation error,plz check your file")
    except ValueError:
        print("Error args")
    finally:
        return result



if __name__ == '__main__':
    main()

