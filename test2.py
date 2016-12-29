# coding=utf-8


class Worker(object):
    good_at = "搬砖"

    def print_info(self):
        print("good at %s" % self.good_at)


wk = Worker()

wk.print_info()
