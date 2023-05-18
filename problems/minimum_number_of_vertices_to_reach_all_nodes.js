/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findSmallestSetOfVertices = function(n, edges) {
    var dag = []; //reverse dag
    for (var i = 0; i < n; i++)
        dag.push([]);
    for (var i = 0; i < edges.length; i++)
        dag[edges[i][1]].push(edges[i][0]);
    var roots = [];
    for (var i = 0; i < dag.length; i++)
        if (dag[i].length == 0)
            roots.push(i);
    return roots;
};