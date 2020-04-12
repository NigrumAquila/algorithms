var getUnique = function(arr) {
    let i = 0, current, length = arr.length, unique = [];
    for(; i < length; i++)
    {
        current = arr[i];
        if(!~unique.indexOf(current))
        {
            unique.push(current);   
        }
    }
    return unique;
}