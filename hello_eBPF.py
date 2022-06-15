#!/usr/bin/python
from bcc import BPF
from time import sleep

program="""
#include <linux/pid_namespace.h>
int writeLog(void *ctx){
	u32 pid = bpf_get_current_pid_tgid();
	struct task_struct *t = (struct task_struct *)bpf_get_current_task();
    u32 upid = t->nsproxy->pid_ns_for_children->last_pid;
    bpf_trace_printk("write call log --> pid=%d; upid=%d!\\n", pid, upid);
	return(0);
}
"""
b=BPF(text=program)

write=b.get_syscall_fnname("write")

b.attach_kprobe(event=write,fn_name="writeLog")
b.trace_print();