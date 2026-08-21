# 📚 Glosario y Guía de Conceptos en Python

Este documento recopila los términos, patrones de diseño y conceptos clave aprendidos durante el desarrollo y consumo de APIs en Python.

---

## 📑 Tabla de Contenidos
1. [Manipulación y Filtrado de Datos](#1-manipulación-y-filtrado-de-datos)
2. [Validación y Control de Flujo](#2-validación-y-control-de-flujo)
3. [Tipos de Datos y Estructuras](#3-tipos-de-datos-y-estructuras)
4. [Manejo de Errores Comunes](#4-manejo-de-errores-comunes)

---

## 1. Manipulación y Filtrado de Datos

### • Dict Comprehension (Comprensión de Diccionarios)
Sintaxis concisa para crear o filtrar un nuevo diccionario a partir de un iterable existente.
```python
datos = {"id": 101, "nombre": "Carlos", "password": "123"}
claves_permitidas = {"id", "nombre"}

# Filtra solo las claves deseadas
datos_filtrados = {k: v for k, v in datos.items() if k in claves_permitidas}
```

### • Whitelist vs. Blacklist
* **Whitelist (Lista blanca):** Estrategia donde explícitamente defines qué campos permitir/incluir. Es la más segura.
* **Blacklist (Lista negra):** Estrategia donde defines qué campos ignorar o excluir (por ejemplo, contraseñas o tokens sensibles).

### • Serialización (json.dumps)
Proceso de convertir un objeto de Python (como diccionarios o listas) en una cadena de texto en formato JSON.

---

## 2. Validación y Control de Flujo

### • Guard Clause (Cláusula de Guarda)
Patrón donde se evalúan condiciones de error o casos inválidos al inicio de una función para salir temprano (`return` o `raise`), evitando anidar bloques `if-else` profundos.
```python
def procesar(valor):
    if not valor:
        return None  # Salida temprana (Guard Clause)
    # Lógica principal continúa aquí...
```

### • Truthy / Falsy
En Python, los valores no solo son booleanos (`True` o `False`). Ciertos valores se evalúan automáticamente como falsos en contextos condicionales:
* **Falsy:** `""` (string vacío), `None`, `0`, `[]` (lista vacía), `{}` (dict vacío).
* **Truthy:** Cualquier string con texto (`"Pikachu"`), números distintos de cero, colecciones con elementos.

### • Limpieza de Cadenas (`.strip()` y `.lower()`)
* **`.strip()`:** Método de cadena que remueve espacios en blanco, saltos de línea y tabulaciones al principio y al final del texto.
* **`.lower()`:** Convierte todo el texto a minúsculas.
* **Encadenamiento de métodos:** Se pueden usar juntos: `texto.strip().lower()`.

### • Control de Bucles (`continue` vs `break`)
* **`break`:** Termina y sale inmediatamente del bucle actual.
* **`continue`:** Salta el resto del código del ciclo actual y regresa de inmediato al inicio de la siguiente iteración del bucle.

---

## 3. Tipos de Datos y Estructuras

### • Diccionarios Anidados (Nested Dictionaries)
Estructuras donde el valor asociado a una clave de un diccionario es otro diccionario.
```python
stat = {
    "base_stat": 45,
    "stat": {
        "name": "hp"
    }
}

# Acceso encadenado:
nombre_stat = stat['stat']['name']  # "hp"
```

---

## 4. Manejo de Errores Comunes

### • `TypeError: unhashable type: 'list'`
Ocurre cuando intentas usar un tipo mutable (como una lista) en un lugar donde Python requiere un valor inmutable / hashable (como la clave de un diccionario o un elemento de un set).
* **Causa común:** Usar comas dentro de corchetes por error: `data['name', data['stats']]` (Python lo interpreta como una tupla `('name', lista)` usada como clave).
* **Solución:** Acceder por separado a cada clave: `data['name']` y `data['stats']`.

### • `AttributeError: 'builtin_function_or_method' object has no attribute '...'`
Ocurre cuando intentas encadenar un método sobre una función a la que olvidaste ponerle paréntesis `()`.
* **Causa:** `input().strip.lower()` (faltan los paréntesis en `strip`).
* **Solución:** `input().strip().lower()`.
