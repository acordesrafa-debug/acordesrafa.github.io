# Web de Acordes Rafa 🎸

Esta es la página web para el canal de YouTube **Acordes Rafa**, diseñada para ser 100% gratuita, de código abierto y optimizada para SEO.

## 🚀 Cómo publicar tu sitio gratis

Para cumplir con tu deseo de no pagar licencias ni hosting, te recomiendo las siguientes opciones:

### 1. GitHub Pages (Recomendado)
Es la opción número uno para proyectos Open Source.
- Crea una cuenta en [GitHub](https://github.com).
- Crea un nuevo repositorio llamado `acordesrafa.github.io`.
- Sube los archivos `index.html` y `styles.css`.
- ¡Listo! Tu web estará en `https://acordesrafa.github.io`.

### 2. Netlify
- Ve a [Netlify](https://www.netlify.com).
- Arrastra y suelta la carpeta `acordes_rafa_web`.
- Te darán un dominio gratis (ej: `acordes-rafa.netlify.app`).

---

## 🛠️ Configuración Final

### Formulario de Contacto y Suscripción
He configurado el sitio para usar **Formspree**, que es gratuito.
1. Ve a [Formspree.io](https://formspree.io) y crea una cuenta gratuita.
2. Crea un nuevo "Form" y copia el ID que te darán.
3. En el archivo `index.html`, busca la línea:
   `<form action="https://formspree.io/f/YOUR_ID" method="POST">`
4. Reemplaza `YOUR_ID` con tu ID de Formspree.

### Feed de YouTube Automático
El sitio ya incluye un embed que muestra la lista de reproducción de tus últimos videos. 
Para que funcione perfectamente con tu canal:
1. Tu ID de canal (Channel ID) es necesario. 
2. En `index.html`, busca el `<iframe>` de YouTube.
3. El parámetro `list=UULFx3IAtH4-itXWv_8m-UOg` debe tener tu ID de lista de cargas. (Normalmente es tu Channel ID cambiando la 'C' por una 'U').

---

## 🔍 Detalles Técnicos
- **Diseño**: Estilo premium oscuro con detalles en madera y ámbar.
- **Responsivo**: Se adapta a móviles, tablets y computadoras.
- **SEO**: Títulos, descripciones y palabras clave ya integrados para posicionar en Google bajo "acordes de guitarra".
- **Sin Licencias**: Solo usa HTML, CSS y fuentes gratuitas de Google Fonts.
