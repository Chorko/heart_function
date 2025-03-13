# ❤️ Heart Function Plot

This script plots a heart-shaped curve using the equation:

```math
x^2 + (y - |x|)^2 = 6
```

## Equation Breakdown  
Rearranging for **y**:

```math
y = |x| \pm \sqrt{6 - x^2}
```

- **Upper curve:**  
  ```math
  y_{\text{upper}} = |x| + \sqrt{6 - x^2}
  ```
- **Lower curve:**  
  ```math
  y_{\text{lower}} = |x| - \sqrt{6 - x^2}
  ```

## Scaling **y** and Its Effects  
| Modification | Effect on Shape |
|-------------|----------------|
| `0.5y`  | **Wider & shorter** (stretched horizontally) |
| `2y`    | **Narrower & taller** |
| `44y`   | **Very thin & compressed vertically** |

## How to Run  
1. Install dependencies:  
   ```sh
   pip install numpy matplotlib
   ```
2. Run the script:  
   ```sh
   python heart.py
   ```
3. A heart-shaped plot will be displayed. ❤️  
![image](https://github.com/user-attachments/assets/e345bced-6837-4bad-8e2f-b720d061f6a8)



---

📌 **Note:**  
- Increasing **y** compresses the shape vertically.  
- Decreasing **y** stretches it horizontally.  

