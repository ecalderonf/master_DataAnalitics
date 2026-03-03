/* DataProject: LógicaConsultasSQL

## Consultas

*/

-- 1. Crea el esquema de la BBDD.

-- 2. Muestra los nombres de todas las películas con una clasificación por edades de ‘Rʼ.
SELECT title 
FROM film
where rating = 'R';

-- 3. Encuentra los nombres de los actores que tengan un 'actor_id' entre 30 y 40.
select a.first_name , a.last_name 
from actor a 
where a.actor_id  between 30 and 40;

-- 4. Obtén las películas cuyo idioma coincide con el idioma original.
select *
from film f 
where f.language_id = f.original_language_id;

-- 5. Ordena las películas por duración de forma ascendente.
select *
from film f 
order by f.length ;

-- 6. Encuentra el nombre y apellido de los actores que tengan ‘Allenʼ en su apellido.
select *
from actor a
where a.first_name LIKE UPPER('%Allen%') or a.last_name LIKE UPPER('%Allen%') ;

-- 7. Encuentra la cantidad total de películas en cada clasificación de la tabla 'film' y muestra la clasificación junto con el recuento.
select f.rating, count(f.film_id ) 
from film f 
group by f.rating;

-- 8. Encuentra el título de todas las películas que son ‘PG-13ʼ o tienen una duración mayor a 3 horas en la tabla 'film'.
select *
from film f 
where f.rating = 'PG-13' or f.length > 180;

-- 9. Encuentra la variabilidad de lo que costaría reemplazar las películas.
SELECT 
    VARIANCE(replacement_cost) AS variabilidad_reemplazo
FROM film;

-- 10. Encuentra la mayor y menor duración de una película de nuestra BBDD.
select min(f.length) as duracion_minima, max(f.length )  as duracion_maxima
from film f ;

-- 11. Encuentra lo que costó el antepenúltimo alquiler ordenado por día.
SELECT 
    rental_id,
    rental_date,
    amount
FROM payment
JOIN rental USING (rental_id)
ORDER BY rental_date DESC
OFFSET 2
LIMIT 1;

-- 12. Encuentra el título de las películas en la tabla 'film' que no sean ni ‘NC-17ʼ ni ‘Gʼ en cuanto a su clasificación.
select f.title 
from film f 
where f.rating not in ('NC-17','G');

-- 13. Encuentra el promedio de duración de las películas para cada clasificación de la tabla 'film' y muestra la clasificación junto con el promedio de duración.
select f.rating, round(avg(f.length),2) as promedio_duracion
from film f 
group by f.rating;

-- 14. Encuentra el título de todas las películas que tengan una duración mayor a 180 minutos.
select f.title 
from film f 
where f.length > 180;

-- 15. ¿Cuánto dinero ha generado en total la empresa?
select sum(p.amount ) 
from payment p  ;

-- 16. Muestra los 10 clientes con mayor valor de id.
select * 
from customer c 
order by c.customer_id desc
limit 10;

-- 17. Encuentra el nombre y apellido de los actores que aparecen en la película con título ‘Egg Igbyʼ.
select a.first_name , a.last_name 
from actor a 
where a.actor_id in (
	select fa.actor_id 
	from film_actor fa
	 	inner join film f 
	 	on fa.film_id = f.film_id 
		where f.title = UPPER('Egg Igby')
);

-- 18. Selecciona todos los nombres de las películas únicos.
SELECT DISTINCT f.title
FROM film f
ORDER BY f.title;

-- 19. Encuentra el título de las películas que son comedias y tienen una duración mayor a 180 minutos en la tabla 'film'.
SELECT f.title 
FROM film AS f 
inner JOIN film_category AS fc 
	ON f.film_id = fc.film_id 
inner JOIN category AS c 
	ON fc.category_id = c.category_id 
	WHERE c.name = 'Comedy' 
AND f.length > 180;

-- 20. Encuentra las categorías de películas que tienen un promedio de duración superior a 110 minutos y muestra el nombre de la categoría junto con el promedio de duración.
SELECT c.name, round(AVG(f.length),2) AS avg_length 
FROM category AS c 
JOIN film_category AS fc 
	ON c.category_id = fc.category_id 
JOIN film AS f 
	ON fc.film_id = f.film_id 
GROUP BY c.category_id, c.name 
HAVING AVG(f.length) > 110;

-- 21. ¿Cuál es la media de duración del alquiler de las películas?
SELECT AVG(return_date - rental_date) AS avg_rental_duration 
FROM rental;


-- 22. Crea una columna con el nombre y apellidos de todos los actores y actrices.
SELECT actor_id, CONCAT(first_name, ' ', last_name) AS full_name 
FROM actor;

-- 23. Número de alquileres por día, ordenados por cantidad de alquiler de forma descendente.
SELECT DATE(rental_date) AS rental_day, COUNT(*) AS total_rentals 
FROM rental 
GROUP BY DATE(rental_date) 
ORDER BY total_rentals DESC;

-- 24. Encuentra las películas con una duración superior al promedio.
select film_id, title, length
FROM film
WHERE length > (
    SELECT AVG(length)
    FROM film
);

-- 25. Averigua el número de alquileres registrados por mes.
SELECT 
    DATE_TRUNC('month', rental_date) AS month,
    COUNT(*) AS total_rentals
FROM rental
GROUP BY DATE_TRUNC('month', rental_date)
ORDER BY month;

-- 26. Encuentra el promedio, la desviación estándar y varianza del total pagado.
SELECT AVG(amount) AS promedio, STDDEV(amount) AS desviacion_estandar, VARIANCE(amount) AS varianza 
FROM payment;

-- 27. ¿Qué películas se alquilan por encima del precio medio?
SELECT 
    f.film_id,
    f.title,
    f.rental_rate
FROM film AS f
WHERE f.rental_rate > (
    SELECT AVG(rental_rate)
    FROM film
);

-- 28. Muestra el id de los actores que hayan participado en más de 40 películas.
SELECT 
    actor_id,
    COUNT(film_id) AS total_films
FROM film_actor
GROUP BY actor_id
HAVING COUNT(film_id) > 40;

-- 29. Obtener todas las películas y, si están disponibles en el inventario, mostrar la cantidad disponible.
SELECT f.film_id, f.title, COUNT(i.inventory_id) AS cantidad_disponible 
FROM film AS f 
LEFT JOIN inventory AS i 
	ON f.film_id = i.film_id 
GROUP BY f.film_id, f.title 
ORDER BY f.title;

-- 30. Obtener los actores y el número de películas en las que ha actuado.
SELECT 
    a.actor_id,
    a.first_name || ' ' || a.last_name AS actor_name,
    COUNT(fa.film_id) AS total_peliculas
FROM actor AS a
JOIN film_actor AS fa
    ON a.actor_id = fa.actor_id
GROUP BY a.actor_id, a.first_name, a.last_name
ORDER BY total_peliculas DESC;

-- 31. Obtener todas las películas y mostrar los actores que han actuado en ellas, incluso si algunas películas no tienen actores asociados.
SELECT f.film_id, f.title, a.actor_id, a.first_name || ' ' || a.last_name AS actor_name 
FROM film AS f 
LEFT JOIN film_actor AS fa 
	ON f.film_id = fa.film_id 
LEFT JOIN actor AS a 
	ON fa.actor_id = a.actor_id 
ORDER BY f.title, actor_name;

-- 32. Obtener todos los actores y mostrar las películas en las que han actuado, incluso si algunos actores no han actuado en ninguna película.
SELECT 
    a.actor_id,
    a.first_name || ' ' || a.last_name AS actor_name,
    f.film_id,
    f.title
FROM actor AS a
LEFT JOIN film_actor AS fa
    ON a.actor_id = fa.actor_id
LEFT JOIN film AS f
    ON fa.film_id = f.film_id
ORDER BY actor_name, f.title;

-- 33. Obtener todas las películas que tenemos y todos los registros de alquiler.
SELECT 
    f.film_id,
    f.title,
    r.rental_id,
    r.rental_date,
    r.return_date
FROM film AS f
LEFT JOIN inventory AS i
    ON f.film_id = i.film_id
LEFT JOIN rental AS r
    ON i.inventory_id = r.inventory_id
ORDER BY f.title, r.rental_date;

-- 34. Encuentra los 5 clientes que más dinero se hayan gastado con nosotros.
SELECT 
    c.customer_id,
    c.first_name || ' ' || c.last_name AS cliente,
    SUM(p.amount) AS total_gastado
FROM customer AS c
JOIN payment AS p
    ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_gastado DESC
LIMIT 5;

-- 35. Selecciona todos los actores cuyo primer nombre es 'Johnny'.
SELECT actor_id, first_name, last_name 
FROM actor 
WHERE first_name = UPPER('Johnny');

-- 36. Renombra la columna 'first_name' como **Nombre** y 'last_name' como **Apellido**.
SELECT 
    first_name AS "Nombre",
    last_name  AS "Apellido"
FROM actor;

-- 37. Encuentra el ID del actor más bajo y más alto en la tabla 'actor'.
SELECT 
    MIN(actor_id) AS id_mas_bajo,
    MAX(actor_id) AS id_mas_alto
FROM actor;

-- 38. Cuenta cuántos actores hay en la tabla 'actor'.
SELECT COUNT(actor_id ) AS total_actores 
FROM actor;

-- 39. Selecciona todos los actores y ordénalos por apellido en orden ascendente.
SELECT 
    actor_id,
    first_name,
    last_name
FROM actor
ORDER BY last_name ASC;

-- 40. Selecciona las primeras 5 películas de la tabla 'film'.
SELECT 
    film_id,
    title
FROM film
ORDER BY film_id
LIMIT 5;

-- 41. Agrupa los actores por su nombre y cuenta cuántos actores tienen el mismo nombre.  
    ¿Cuál es el nombre más repetido?
 SELECT first_name AS nombre, COUNT(*) AS total_actores
FROM actor
GROUP BY first_name
ORDER BY total_actores DESC;

-- 42. Encuentra todos los alquileres y los nombres de los clientes que los realizaron.

-- 43. Muestra todos los clientes y sus alquileres si existen, incluyendo aquellos que no tienen alquileres.

-- 44. Realiza un CROSS JOIN entre las tablas 'film' y 'category'.  
    ¿Aporta valor esta consulta?  
    ¿Por qué?  
    Deja después de la consulta la contestación.

-- 45. Encuentra los actores que han participado en películas de la categoría 'Action'.

-- 46. Encuentra todos los actores que no han participado en películas.

-- 47. Selecciona el nombre de los actores y la cantidad de películas en las que han participado.

-- 48. Crea una vista llamada 'actor_num_peliculas' que muestre los nombres de los actores y el número de películas en las que han participado.

-- 49. Calcula el número total de alquileres realizados por cada cliente.

-- 50. Calcula la duración total de las películas en la categoría 'Action'.

-- 51. Crea una tabla temporal llamada 'cliente_rentas_temporal' para almacenar el total de alquileres por cliente.

-- 52. Crea una tabla temporal llamada 'peliculas_alquiladas' que almacene las películas que han sido alquiladas al menos 10 veces.

-- 53. Encuentra el título de las películas que han sido alquiladas por el cliente con el nombre 'Tammy Sanders' y que aún no se han devuelto.  
    Ordena los resultados alfabéticamente por título de película.

-- 54. Encuentra los nombres de los actores que han actuado en al menos una película que pertenece a la categoría 'Sci-Fi'.  
    Ordena los resultados alfabéticamente por apellido.

-- 55. Encuentra el nombre y apellido de los actores que han actuado en películas que se alquilaron después de que la película 'Spartacus Cheaper' se alquilara por primera vez.  
    Ordena los resultados alfabéticamente por apellido.

-- 56. Encuentra el nombre y apellido de los actores que no han actuado en ninguna película de la categoría 'Music'.

-- 57. Encuentra el título de todas las películas que fueron alquiladas por más de 8 días.

-- 58. Encuentra el título de todas las películas que son de la misma categoría que 'Animation'.

-- 59. Encuentra los nombres de las películas que tienen la misma duración que la película con el título 'Dancing Fever'.  
    Ordena los resultados alfabéticamente por título de película.

-- 60. Encuentra los nombres de los clientes que han alquilado al menos 7 películas distintas.  
    Ordena los resultados alfabéticamente por apellido.

-- 61. Encuentra la cantidad total de películas alquiladas por categoría y muestra el nombre de la categoría junto con el recuento de alquileres.

-- 62. Encuentra el número de películas por categoría estrenadas en 2006.

-- 63. Obtén todas las combinaciones posibles de trabajadores con las tiendas que tenemos.

-- 64. Encuentra la cantidad total de películas alquiladas por cada cliente y muestra el ID del cliente, su nombre y apellido junto con la cantidad de películas alquiladas.
