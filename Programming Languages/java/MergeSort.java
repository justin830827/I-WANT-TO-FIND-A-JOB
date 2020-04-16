public class MergeSort {

    private int[] array;
    private int[] tempArr;
    private int n;

    public static void main(String a[]) {

        int[] inputArr = { 45, 23, 11, 89, 77, 98, 4, 28, 65, 43 };
        MergeSort mms = new MergeSort();
        mms.sort(inputArr);
        for (int i : inputArr) {
            System.out.print(i);
            System.out.print(" ");
        }
    }

    public void sort(int inputArr[]) {
        this.array = inputArr;
        this.n = inputArr.length;
        this.tempArr = new int[n];
        doMergeSort(0, n - 1);
    }

    private void doMergeSort(int left, int high) {

        if (left < high) {
            int middle = left + (high - left) / 2;
            // Below step sorts the left side of the array
            doMergeSort(left, middle);
            // Below step sorts the right side of the array
            doMergeSort(middle + 1, high);
            // Now merge both sides
            merge(left, middle, high);
        }
    }

    private void merge(int left, int middle, int high) {

        for (int i = left; i < high; i++) {
            tempArr[i] = array[i];
        }
        int i = left;
        int j = middle + 1;
        int k = left;
        while (i < middle && j < high) {
            if (tempArr[i] <= tempArr[j]) {
                array[k] = tempArr[i];
                i++;
            } else {
                array[k] = tempArr[j];
                j++;
            }
            k++;
        }
        while (i < middle) {
            array[k] = tempArr[i];
            k++;
            i++;
        }

        while (j < high) {
            array[k] = tempArr[i];
            k++;
            j++;
        }

    }
}