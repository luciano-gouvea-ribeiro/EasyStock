const API_BASE = "http://127.0.0.1:8000/api/v1/products";

const productsContainer = document.getElementById("productsContainer");
const pageInfo = document.getElementById("pageInfo");

const prevPageButton = document.getElementById("prevPage");
const nextPageButton = document.getElementById("nextPage");

const SEARCH_URL = `${API_BASE}`;
const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");

const productForm = document.getElementById("productForm");

const nomeInput = document.getElementById("nome");
const skuInput = document.getElementById("sku");
const codigoBarrasInput = document.getElementById("codigo_barras");
const precoCustoInput = document.getElementById("preco_custo");
const precoVendaInput = document.getElementById("preco_venda");
const quantidadeInput = document.getElementById("quantidade");
const estoqueMinimoInput = document.getElementById("estoque_minimo");
const estoqueMaximoInput = document.getElementById("estoque_maximo");

let currentPage = 1;
const limit = 5;

function renderProducts(products) {
    productsContainer.innerHTML = "";

    products.forEach(product => {
        const productCard = document.createElement("div");
        productCard.classList.add("product-card");

        productCard.innerHTML = `
            <h3>${product.nome}</h3>
            <p><strong>SKU:</strong> ${product.sku}</p>
            <p><strong>Preço:</strong> R$ ${product.preco_venda}</p>
            <p><strong>Quantidade:</strong> ${product.quantidade}</p>
            <div class="card-actions">
                <button data-action="edit" data-id="${product.id}">Editar</button>
                <button data-action="delete" data-id="${product.id}">Deletar</button>
                <button data-action="entrada" data-id="${product.id}">Entrada</button>
                <button data-action="saida" data-id="${product.id}">Saída</button>
            </div>
        `;

        productsContainer.appendChild(productCard);
    });

    // attach event listeners for action buttons
    productsContainer.querySelectorAll("button").forEach(btn => {
        btn.addEventListener("click", async (e) => {
            const action = btn.getAttribute("data-action");
            const id = btn.getAttribute("data-id");

            if (action === "edit") await handleEdit(id);
            if (action === "delete") await handleDelete(id);
            if (action === "entrada") await handleMovement(id, "entrada");
            if (action === "saida") await handleMovement(id, "saida");
        });
    });
}

async function loadProducts(page = 1) {
    try {
        const response = await fetch(`${API_BASE}/paginated?page=${page}&limit=${limit}`);
        const products = await response.json();

        renderProducts(products);

        pageInfo.innerText = `Página ${page}`;
        currentPage = page;
    } catch (error) {
        console.error("Erro ao carregar produtos:", error);
        productsContainer.innerHTML = "<p>Não foi possível carregar produtos.</p>";
    }
}

async function searchProducts() {
    const productName = searchInput.value.trim();

    if (productName === "") {
        loadProducts(1);
        return;
    }

    try {
        const response = await fetch(`${SEARCH_URL}?product_name=${encodeURIComponent(productName)}`);
        const products = await response.json();

        renderProducts(products);
        pageInfo.innerText = "Resultado da busca";
    } catch (error) {
        console.error("Erro ao buscar produtos:", error);
    }
}

async function createProduct(event) {
    event.preventDefault();

    const productData = {
        nome: nomeInput.value,
        sku: skuInput.value,
        codigo_barras: codigoBarrasInput.value || null,
        preco_custo: Number(precoCustoInput.value),
        preco_venda: Number(precoVendaInput.value),
        quantidade: Number(quantidadeInput.value),
        estoque_minimo: Number(estoqueMinimoInput.value),
        estoque_maximo: estoqueMaximoInput.value ? Number(estoqueMaximoInput.value) : null
    };

    try {
        const response = await fetch(`${API_BASE}/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(productData)
        });

        if (!response.ok) {
            const error = await response.json();
            alert(error.detail || "Erro ao cadastrar produto");
            return;
        }

        alert("Produto cadastrado com sucesso!");
        productForm.reset();
        loadProducts(1);
    } catch (error) {
        console.error("Erro ao cadastrar produto:", error);
        alert("Erro ao conectar com a API.");
    }
}

async function handleEdit(id) {
    try {
        const resp = await fetch(`${API_BASE}/${id}`);
        if (!resp.ok) return alert("Produto não encontrado");

        const product = await resp.json();

        const nome = prompt("Nome:", product.nome) || product.nome;
        const preco_venda = prompt("Preço de venda:", product.preco_venda) || product.preco_venda;

        const updateData = {
            nome: nome,
            preco_venda: Number(preco_venda)
        };

        const updateResp = await fetch(`${API_BASE}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(updateData)
        });

        if (!updateResp.ok) {
            const err = await updateResp.json();
            return alert(err.detail || "Erro ao atualizar produto");
        }

        alert("Produto atualizado");
        loadProducts(currentPage);
    } catch (error) {
        console.error(error);
    }
}

async function handleDelete(id) {
    if (!confirm("Confirma exclusão do produto?")) return;

    try {
        const resp = await fetch(`${API_BASE}/${id}`, { method: "DELETE" });
        if (!resp.ok) {
            const err = await resp.json();
            return alert(err.detail || "Erro ao deletar produto");
        }

        alert("Produto deletado");
        loadProducts(1);
    } catch (error) {
        console.error(error);
    }
}

async function handleMovement(id, type) {
    const qty = Number(prompt(`Quantidade para ${type}:`, ""));
    if (!qty || qty <= 0) return alert("Quantidade inválida");

    try {
        const resp = await fetch(`${API_BASE}/${id}/${type}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ quantidade: qty })
        });

        if (!resp.ok) {
            const err = await resp.json();
            return alert(err.detail || "Erro na movimentação");
        }

        const data = await resp.json();
        alert(data.message || "Movimentação realizada");
        loadProducts(currentPage);
    } catch (error) {
        console.error(error);
    }
}

productForm.addEventListener("submit", createProduct);
searchButton.addEventListener("click", searchProducts);
searchInput.addEventListener("keypress", (event) => { if (event.key === "Enter") searchProducts(); });
prevPageButton.addEventListener("click", () => { if (currentPage > 1) loadProducts(currentPage - 1); });
nextPageButton.addEventListener("click", () => { loadProducts(currentPage + 1); });

loadProducts();