import threading
import queue

class Thread_Manage():
    def __init__(self):
        self.thread_management = {}

    def manage(self):
        all_registered_thread_name = self.all_thread_name
        #print("{0}: {1} Threads Remain\n".format(self.__class__.__name__, all_registered_thread_name))
        #print("{0}: {1} Threads Remain\n".format(self.__class__.__name__, len(all_registered_thread_name)))
        for thread_name in all_registered_thread_name:
            fd = self.get_thread_fd(thread_name)
            if not fd.is_alive():
                self.deregister(thread_name)
                print("{0}: Thread {1} Deregister".format(self.__class__.__name__, thread_name))
        return self.all_thread_name

    # 注册线程
    def register(self, thread_name, thread_target, *args):
        if thread_name not in self.thread_management.keys():
            self.thread_management[thread_name] = {}
            thread_queue = queue.Queue()
            self.thread_management[thread_name]['queue'] = thread_queue
            # 变长参数args，其中第一个参数一定时queue
            args_list = [thread_queue, thread_name]
            for arg in args:
                args_list.append(arg)
            args = tuple(args_list)
            # 创建线程，并传入变长参数
            thread_fd = threading.Thread(target=thread_target, args=args)
            print(thread_fd)
            self.thread_management[thread_name]['fd'] = thread_fd
            self.thread_management[thread_name]['running_flag'] = True
            return True
        else:
            return False

    # 注销线程
    def deregister(self, thread_name):
        if thread_name in self.thread_management.keys():
            del self.thread_management[thread_name]
            return True
        else:
            return False

    # 获取所有已注册的线程
    @property
    def all_thread_name(self):
        return [thread_name for thread_name in self.thread_management.keys()]

    # 获取线程fd
    def get_thread_fd(self, thread_name):
        if thread_name in self.thread_management.keys():
            return self.thread_management[thread_name]['fd']
        else:
            return False

    # 获取线程允许标志
    def get_flag(self, thread_name):
        if thread_name in self.thread_management.keys():
            return self.thread_management[thread_name]['running_flag']
        else:
            return False

    # 通过设置线程运行标志	False来销毁线程
    def stop(self, thread_name):
        if thread_name in self.thread_management.keys():
            self.thread_management[thread_name]['running_flag'] = False
            return True
        else:
            return False

    # 获取线程queue
    def get_thread_queue(self, thread_name):
        if thread_name in self.thread_management.keys():
            return self.thread_management[thread_name]['queue']
        else:
            return False

    # 给线程发送信息
    def send_to(self, thread_name, msg):
        if thread_name in self.thread_management.keys():
            queue = self.thread_management[thread_name]['queue']
            queue.put(msg)

    # 启动线程
    def activate(self, thread_name, deamon=True):
        task_thread_fd = self.get_thread_fd(thread_name)
        if task_thread_fd:
            if deamon:
                task_thread_fd.setDaemon(True)
            task_thread_fd.start()
            print("Thread %r Start" % thread_name)
            return True
        else:
            return False

    # 通过设置线程运行标志	False来销毁线程
    def terminate(self, thread_name):
        thread_queue = self.get_thread_queue(thread_name)
        task_thread_fd = self.get_thread_fd(thread_name)
        if task_thread_fd and thread_queue:
            # 设置flag为False，线程轮询flag时可结束线程
            self.stop(thread_name)
            self.deregister(thread_name)
            return True
        else:
            return False

    # 判断线程运行
    def ifAlive(self, thread_name):
        task_thread_fd = self.get_thread_fd(thread_name)
        if task_thread_fd:
            return task_thread_fd.is_alive()
        else:
            return False

    # 同步线程
    def to_join(self, thread_name):
        task_thread_fd = self.get_thread_fd(thread_name)
        if task_thread_fd:
            task_thread_fd.join(30)
            self.deregister(thread_name)
            print('thread %r has joined' % thread_name)
            return True
        else:
            return False

    def join(self, thread_name):
        task_thread_fd = self.get_thread_fd(thread_name)
        if task_thread_fd:
            task_thread_fd.join(30)
            print('thread %r has joined' % thread_name)
            return True
        else:
            return False

    # 结束所有的线程
    def all_terminate(self):
        all_thread_name = self.all_thread_name
        print("{0} Try to end threads:{1}".format(self.__class__.__name__, all_thread_name))
        for thread_name in all_thread_name:
            print('{0} Try to end {1} thread'.format(self.__class__.__name__, thread_name))
            try:
                # 该函数仅仅是将运行标志修改为False，并通过queue发送quit命令给thread
                self.terminate(thread_name)
            except Exception as e:
                print("{0} ServiceStop error: ".format(self.__class__.__name__))
        return True
