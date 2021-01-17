package com.yuntao.practise.queue;

public class CircularQueue {
    private int[] array;
    private int size;
    private int space;
    private int head = 0;
    private int tail = 0;

    public CircularQueue(int k) {
        // verify k > 1
        this.array = new int[k+1];
        this.size = k;
        this.space = k + 1;
    }

    public boolean enQueue(int value) {
        if(isFull()){
            return false;
        } else {
            array[tail] = value;
            tail = (tail + 1) % space;
            return true;
        }
    }

    public boolean deQueue() {
        if(isEmpty()){
            return false;
        } else {
            head = (head + 1) % space;
            return true;
        }
    }

    public int Front() {
        if(isEmpty()){
            return -1;
        } else {
            return array[head];
        }
    }

    public int Rear() {
        if(isEmpty()){
            return -1;
        } else {
            return array[(tail + size) % space];
        }
    }

    public boolean isEmpty() {
        return head == tail;
    }

    public boolean isFull() {
        return (tail + 1) % space == head;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
