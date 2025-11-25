# Diseño de Clases - Hundir la Flota

## Diagrama UML (Mermaid)

```mermaid
classDiagram
    class Barco {
        +String nombre
        +int longitud
        +int golpes_recibidos
        +__init__(nombre, longitud)
        +recibir_impacto()
        +esta_hundido() bool
        +mostrar_estado()
    }

    class Tablero {
        +int dimensiones
        +List casillas
        +__init__(tamano)
        +mostrar_tablero()
    }
