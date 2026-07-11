class DynamicArray {
    private int[] arr;
    // capacity == arr.length
    private int size;

    public DynamicArray(int capacity) {
        this.arr = new int[capacity];
        this.size = 0;
    }

    public int get(int i) {
        return this.arr[i];
    }

    public void set(int i, int n) {
        this.arr[i] = n;
    }

    public void pushback(int n) {
        if (this.size == this.arr.length) {
            this.resize();
        }
        this.arr[this.size++] = n;
    }

    public int popback() {
        return this.arr[--this.size];
    }

    private void resize() {
        int[] doubled = new int[2 * this.arr.length];
        for (int i = 0; i < this.arr.length; i++) {
            doubled[i] = this.arr[i];
        }
        this.arr = doubled;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.arr.length;
    }
}
