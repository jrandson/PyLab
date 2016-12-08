
def get_c(c):
	ch = 'abcdefghijklmnopqrstuvwxyz'
	c2 = ' '
	for i in range(len(ch)):		
		if ch[i] == c:
			j = (i+2) % len(ch)
			c2 = ch[j]
			break	

	return c2

l = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
l1 = "that's a handy little function. isn't it?"
l2 = ''

for c  in l1:
	l2 += get_c(c)

print l2