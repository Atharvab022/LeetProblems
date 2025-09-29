class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int rowstart=0;
        int colstart=0;
        int rowend=matrix.length-1;
        int colend=matrix[0].length-1;
        List<Integer> l=new ArrayList<>();
        while(rowstart<=rowend && colstart<=colend){
            for(int i=colstart;i<=colend;i++){
                l.add(matrix[rowstart][i]);
            }
            rowstart++;
            for(int i=rowstart;i<=rowend;i++){
                l.add(matrix[i][colend]);

            }
            colend--;
            if(rowstart<=rowend){
            for(int i=colend;i>=colstart;--i){
                l.add(matrix[rowend][i]);
            }
            rowend--;
            }
            if(colstart<=colend){
            for(int i=rowend;i>=rowstart;--i){
                l.add(matrix[i][colstart]);
            }
            colstart++;
            }


        }
        return l;
    }
}