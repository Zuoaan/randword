import random,argparse,sys

Lower_base = list("qwertyuiopasdfghjklzxcvbnm")
Upper_base = list("QWERTYUIOPASDFGHJKLZXCVBNM")
Number_base = list("1234567890")
#If you want more,you can add other base.

def born(lenth,soup):
    """不重复抽取，长度 : lenth"""
    return ''.join(random.sample(soup,lenth))

def bornRe(lenth,soup):
    """重复抽取，长度 : lenth"""
    return ''.join(random.choices(soup,k=lenth))

if __name__=="__main__":
    parser = argparse.ArgumentParser(
        description="Born your password!",
        epilog="e.g. randword -l 10 -L -U -N")
    parser.add_argument("-l","--lenth",
        type=int,required=True,help="Lenth of your word(长度)")
    parser.add_argument("-a","--add",
        type=str,default=None,help="Add other base.")
    parser.add_argument("-t","--times",
        type=int,default=1,help="I need more.")
    parser.add_argument("-s","--seed",
        type=int,default=None,help="Set the seed.")
    parser.add_argument("-r","--re",
        action='store_true',help="Re.")
    parser.add_argument("-L","--Lower",
        action='store_true',help="Lower one.")
    parser.add_argument("-U","--Upper",
        action='store_true',help="Upper one.")
    parser.add_argument("-N","--Number",
        action='store_true',help="Number.")
    
    args = parser.parse_args()
    if args.lenth <=0:
        sys.exit()
    if args.seed:
        random.seed(args.seed)
    soup = []
    if args.Lower:
        soup+=Lower_base
    if args.Upper:
        soup+=Upper_base
    if args.Number:
        soup+=Number_base
    if soup:
        for i in range(args.times):
            if args.re:
                answer = bornRe(args.lenth,soup)
            else:
                answer = born(args.lenth,soup)
            print(answer)
    else:
        sys.exit()
        
    
