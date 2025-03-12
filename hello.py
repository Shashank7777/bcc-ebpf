#!/usr/bin/python

from bcc import BPF

BPF(text='int kprobe__sys_clone(void *ctx) {bpf_trace_printk("Hello, World!\\n"); return 0; }').trace_print()

# int kprobe__sys_clone(void *ctx) -> Defines a kprobe handler that hooks into sys_clone. The parameter contains CPU register values at the time of the call.

#bpf_trace_printk("Hello World") -> Sends Hello World to the BPF trace buffer whenever the sys_clone function is executed.

