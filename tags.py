1 content of weibo: feed_list_content

rule=r'"feed_list_content\\" >\\n.*?<\\/div>\\n'
rule=r'feed_list_content.*?<\\/div>\\n'

## http://www.weibo.com/p/1003061235457821/weibo
2 page_id: \r\n$CONFIG[\'page_id\']=\'1003061235457821\'; 
		   \r\n$CONFIG[\'page_id\']=\'1002061642088277\'
		   \r\n$CONFIG[\'page_id\']=\'1003061235457821\'; 

rule = 'page_id.*?;

  <a href=\\"http:\\/\\/weibo.com\\/p\\/1002061642088277\\/

3 userID: \r\n$CONFIG[\'oid\']=\'1235457821\'; 

rule = r'owner_uid=.*?&'


4 username: \r\n$CONFIG[\'onick\']=\'\xe8\x8c\x85\xe4\xba\x8e\xe8\xbd\xbc\';

rule = r'onick.*;'

5 search: http://s.weibo.com/weibo/%25E9%2599%2588%25E5%25BF%2597%25E6%25AD%25A6?topnav=1&wvr=5&b=1
		  http://s.weibo.com/weibo/%25E5%25AD%2599%25E7%25AB%258B%25E5%25B9%25B3?topnav=1&wvr=5&b=1

		  uid=\\"1222713954\\" action-type=\\"follow\\"

		  rule = r'uid=.*?action-type=\\"follow\\"'
		  rule = r'color:red.*?<\\/p>\\n'

print u"\uff0c\u97e9\u6bd3\u6d77\u7684\u6587\u7ae0"

my_unicode = u'\u674e\u5317\u65b9'
my_utf8 = my_unicode.encode('utf-8')
my_utf8
print my_utf8


json_str = '"\\u8fd9\\u5bb6\\u62a5\\u7eb8\\u5728"' # this is a json Obj
json_unicode = json.loads(json_str) # convert json to unicode
json_str_utf8 = json_unicode.encode('utf-8')
print json_str_utf8

unicode(cs,'utf-8') #utf-8 unicode

rule_C = "[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%\"\_\。\，\》\《]"
"李北方，韩毓海的文章，而且李北方的文章还在头版，标题很醒目。仔细翻了一下版的《互联网大佬背后的控制者》，
写得不解渴。版刘继兴写的徐树铮小传倒很有意思。我猜总编肯定是个女的，整不好还是位大美女 "_" "酷" "酷" "" ，
果然如此，总编张亚丽思路开阔，不拘一格。