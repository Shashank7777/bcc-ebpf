#!/usr/bin/python

from bcc import BPF

BPF(text='int kprobe__sys_sync(void *ctx) {bpf_trace_printk("sys_sync() Function Called.!\\n"); return 0; }').trace_print()