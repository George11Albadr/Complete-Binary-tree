# Heap Sort in python


def heapy(arr, n, i):
      # Encuentro los mayores nodos entre los hijos
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
  
      # Se va cambiando con el más grande
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapy(arr, n, largest)
  
  
def heapS(arr):
      n = len(arr)
  
      # se crea
      for i in range(n//2, -1, -1):
          heapy(arr, n, i)
  
      for i in range(n-1, 0, -1):
          # cambio
          arr[i], arr[0] = arr[0], arr[i]
  
          
          heapy(arr, i, 0)
  
  
arr = [1, 12, 9, 5, 6, 10]
heapS(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d " % arr[i], end='')
  
