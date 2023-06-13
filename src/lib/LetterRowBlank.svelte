<script>

    const classBasic = "letter-box filled-box"

</script>

<div class="letter-row">
    <div class={classBasic} > </div>
    <div class={classBasic} > </div>
    <div class={classBasic} > </div>
    <div class={classBasic} > </div>
    <div class={classBasic} > </div>
</div>

<style>

    .filled-box {
        border: 2px solid black;
    }

    .letter-row {
        display: flex;
    }

    .letter-box {
        border: 2px solid gray;
        border-radius: 3px;
        margin: 2px;
        font-size: 2rem;
        font-weight: 700;
        height: 3rem;
        width: 3rem;
        display: flex;
        justify-content: center;
        align-items: center;
        text-transform: uppercase;
    }
</style>