# BUAA-GPA-Calculator
This calculator strictly obeys the official published calculating method which can be found on BUAA Computer Science Department site.

------

### To start using…

[Download](https://github.com/SprLau/BUAA-GPA-Calculator/releases/tag/1.0) from **Releases**.

> Currently, only Unix-like systems are supported.

Or open **Terminal** or **cmd** and run:

```bash
python buaa_gpa.py
```

### To use by importing scores from a file…

1. Create a file named whatever you like; for clarifying, here I use `score.txt`.

2. Edit `score.txt` and make it a gradebook like this:

   ```
   Operating Systems
   100
   4
   Social Computing
   90
   2
   博雅
   A
   0.5
   ```

   where for each set of score: 

   * the first line is the ***course’s name***;

   * the second line is the ***score***:

     * if this is a 5-scale course, let `A` represents 优秀, `B` represents 良好, `C` represents 中等, `D` represents 及格, `E` represents 不及格;
     * if this is a 100-percentile course, just type in your score out of 100.

   * and the third line is the corresponding ***credit***.

     > An example for the gradebook’s syntax: [score.txt](./example/score.txt)

3. If the file is successfully imported, you’ll see:

   ```
   *** File Successfully Added. ***
   ```

   Then you’ll be able to get your GPA from the file:

   ```
   #######################################
   # 1. Add a series of scores;          #
   # 2. Add a single score;              #
   # 3. Get Weighted Average;            #
   # 4. Get Raw Average;                 #
   # 5. Get BUAA GPA;                    #
   # 6. Exit.                            #
   #######################################
   Option: 1
   #######################################
   # 1. Manuelly add;                    #
   # 2. Add from an existed file.        #
   #######################################
   Option: 2
   Filename: score.txt
   *** File Successfully Added. ***
   Option: 5
   The GPA is: 3.9423
   ```

   As well as your average scores (weighted and raw):

   ```
   Option: 3
   The Weighted Ave. : 96.9231
   Option: 4
   The Raw Ave. : 96.6667
   ```

4. After the calculation is done, there will be a `store.txt` that records your history. In most of the cases, pay no attention to it unless you tryna check if there was a mis-input or something like that.
