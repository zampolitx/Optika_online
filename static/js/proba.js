function myPromise()
{
    return new Promise(function(resolve, reject)
    {
        //псевдо асинхронный код
        var ascync = true; //или  false
        if (!ascync)
        return reject(new Error("не удалось выполнить..."));

        return resolve(1);
    });
}

myPromise()
.then(function(res)
{
    console.log(res); //выведет 1
})
.catch(function(err){
    console.log(err.message); //выведет сообщение "не удалось выполнить..."
});