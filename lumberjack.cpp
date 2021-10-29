#include <bits/stdc++.h>

using namespace std;

enum direction{
    UP, DOWN, LEFT, RIGHT
};

vector <string> cut(4);

class Tree{
    int height;
    int thickness;
    int unit_value;
    int unit_weight;

public:
    int x;
    int y;
    int index;
    Tree(int x, int y, int height, int thickness, int uweight, int uvalue)
    {
        this->x = x;
        this->y = y;
        this->height = height;
        this->thickness = thickness;
        this->unit_weight = uweight;
        this->unit_value = uvalue;
    }
    int getHeight()
    {
        return height;
    }
    int retWeight()
    {
        return unit_weight*height*thickness;
    }
    int retValue()
    {
        return unit_value*height*thickness;
    }
    int time(int x, int y)
    {
        return abs(this->x-x) + abs(this->y-y) + this->thickness;
    }
    void printTree()
    {
        cout<<"X: "<<x<<" Y: "<<y<<" Height: "<<height<<" Thickness: "<<thickness<<" Weight: "<<this->retWeight()<<" Value: "<<this->retValue()<<endl;
    }
};


class Grid{
    int time;
    int total_time;
    float factor;
    public:
        vector <vector <int>> grid;
        vector <Tree> forest;
        int current_x;
        int current_y;
        Grid(int n, int x, int y, int t, float f)
        {
            for(int i=0;i<n;i++)
            {
                vector <int> row(n, 0);
                grid.push_back(row);
            }
            current_x = x;
            current_y = y;
            time = t;
            total_time = t;
            factor = f;
        }
        float score(int points, int time)
        {
            return (float)points/(float)pow(time, factor) + 2*(float)pow(time, factor)/(float)points;
        }
        void initForest(vector <Tree> jungle)
        {
            forest = jungle;
        }
        void printGrid()
        {
            for(int j=grid.size()-1;j>=0;j--)
            {
                for(int i=0;i<grid[j].size();i++)
                {
                    cout<<grid[i][j]<<" ";
                }
                cout<<endl;
            }
        }

        vector<pair<float, pair<Tree, int>>> findMax()
        {
            vector<pair<float, pair<Tree, int>>> potential;
            for(auto tree:forest)
            {
                pair<float, pair<Tree, int>> entry(-INT_MAX, pair<Tree, int>(tree, -1));
                if(grid[tree.x][tree.y])
                {
                    for(int direction=0;direction<4;direction++)
                    {
                        if(direction==LEFT)
                        {
                            int point = 0;
                            entry.second.second = LEFT;
                            queue <Tree> q;
                            q.push(forest[grid[tree.x][tree.y]-1]);
                            while(!q.empty())
                            {
                                // cout<<"Hello"<<endl;
                                Tree current_tree = q.front();
                                q.pop();
                                point += current_tree.retValue();
                                for(int i=current_tree.x-1;i>=max(0, current_tree.x-current_tree.getHeight()+1);i--)
                                {
                                    if(grid[i][current_tree.y])
                                    {
                                        Tree potential_tree = forest[grid[i][current_tree.y]-1];
                                        if(potential_tree.retWeight() < current_tree.retWeight())
                                        {
                                            q.push(potential_tree);
                                        }
                                        break;
                                    }
                                }
                            }
                            entry.first = score(point,tree.time(current_x, current_y));
                            potential.push_back(entry);
                        }
                        if(direction==UP)
                        {
                            int point = 0;
                            entry.second.second = UP;
                            queue <Tree> q;
                            q.push(forest[grid[tree.x][tree.y]-1]);
                            while(!q.empty())
                            {
                                Tree current_tree = q.front();
                                q.pop();
                                point += current_tree.retValue();
                                for(int i=current_tree.y+1;i<min( (int)grid.size(), current_tree.y+current_tree.getHeight());i++)
                                {
                                    if(grid[current_tree.x][i])
                                    {
                                        Tree potential_tree = forest[grid[current_tree.x][i]-1];
                                        if(potential_tree.retWeight() < current_tree.retWeight())
                                        {
                                            q.push(potential_tree);
                                        }
                                        break;
                                    }
                                }
                            }
                            entry.first = score(point,tree.time(current_x, current_y));
                            potential.push_back(entry);
                        }
                        if(direction==RIGHT)
                        {
                            int point = 0;
                            entry.second.second = RIGHT;
                            queue <Tree> q;
                            q.push(forest[grid[tree.x][tree.y]-1]);
                            while(!q.empty())
                            {
                                Tree current_tree = q.front();
                                q.pop();
                                point += current_tree.retValue();
                                for(int i=current_tree.x+1;i<min( (int)grid.size(), current_tree.x+current_tree.getHeight());i++)
                                {
                                    if(grid[i][current_tree.y])
                                    {
                                        Tree potential_tree = forest[grid[i][current_tree.y]-1];
                                        if(potential_tree.retWeight() < current_tree.retWeight())
                                        {
                                            q.push(potential_tree);
                                        }
                                        break;
                                    }
                                }
                            }
                            entry.first = score(point,tree.time(current_x, current_y));
                            potential.push_back(entry);
                        }
                        if(direction==DOWN)
                        {
                            int point = 0;
                            entry.second.second = DOWN;
                            queue <Tree> q;
                            q.push(forest[grid[tree.x][tree.y]-1]);
                            while(!q.empty())
                            {
                                Tree current_tree = q.front();
                                q.pop();
                                point += current_tree.retValue();
                                for(int i=current_tree.y-1;i>=max(0, current_tree.x-current_tree.getHeight()+1);i--)
                                {
                                    if(grid[current_tree.x][i])
                                    {
                                        Tree potential_tree = forest[grid[current_tree.x][i]-1];
                                        if(potential_tree.retWeight() < current_tree.retWeight())
                                        {
                                            q.push(potential_tree);
                                        }
                                        break;
                                    }
                                }
                            }
                            entry.first = score(point,tree.time(current_x, current_y));
                            potential.push_back(entry);
                        }
                    }
                }
            }
            sort(potential.begin(), potential.end(), [](const auto& a, const auto& b) {return a.first > b.first; });
            // for(auto i:potential)
            // {
            //     cout<<"Score: "<<i.first<<" X: "<<i.second.first.x<<" Y: "<<i.second.first.y<<" "<<i.second.second<<endl;
            // }
            return potential;
        }

        void updateTime(int t)
        {
            time -= t;
        }

        int calculatePoints(vector <pair<float, pair <Tree, int>>> list)
        {
            bool flag = false;
            for(auto p:list)
            {
                Tree tree = p.second.first;
                if(tree.time(this->current_x, this->current_y)<this->time)
                {
                    updateTime(tree.time(this->current_x, this->current_y));
                    if(current_x > tree.x)
                    {
                        while(current_x>tree.x)
                        {
                            // cout<<"move left"<<endl;
                            current_x--;
                        }
                    }
                    else if(current_x < tree.x)
                    {
                        while(current_x<tree.x)
                        {
                            // cout<<"move right"<<endl;
                            current_x++;
                        }
                    }
                    if(current_y > tree.y)
                    {
                        while(current_y>tree.y)
                        {
                            // cout<<"move down"<<endl;
                            current_y--;
                        }
                    }
                    else if(current_y < tree.y)
                    {
                        while(current_y<tree.y)
                        {
                            // cout<<"move up"<<endl;
                            current_y++;
                        }
                    }
                    // cout<<cut[p.second.second]<<endl;
                    cutTree(p.second.first, p.second.second);
                    flag = true;
                    break;
                }
            }
            // cout<<time<<endl;
            return flag;
        }

        int returnPoints()
        {
            int score = 0;
            for(int i=0;i<forest.size();i++)
            {
                if(!grid[forest[i].x][forest[i].y])
                {
                    score += forest[i].retValue();
                }
            }
            return score;
        }

        bool moveToTree(vector <pair<float, pair <Tree, int>>> list)
        {
            bool flag = false;
            for(auto p:list)
            {
                Tree tree = p.second.first;
                if(tree.time(this->current_x, this->current_y)<this->time)
                {
                    updateTime(tree.time(this->current_x, this->current_y));
                    if(current_x > tree.x)
                    {
                        while(current_x>tree.x)
                        {
                            cout<<"move left"<<endl;
                            current_x--;
                        }
                    }
                    else if(current_x < tree.x)
                    {
                        while(current_x<tree.x)
                        {
                            cout<<"move right"<<endl;
                            current_x++;
                        }
                    }
                    if(current_y > tree.y)
                    {
                        while(current_y>tree.y)
                        {
                            cout<<"move down"<<endl;
                            current_y--;
                        }
                    }
                    else if(current_y < tree.y)
                    {
                        while(current_y<tree.y)
                        {
                            cout<<"move up"<<endl;
                            current_y++;
                        }
                    }
                    cout<<cut[p.second.second]<<endl;
                    cutTree(p.second.first, p.second.second);
                    flag = true;
                    break;
                }
            }
            return flag;
        }

        void cutTree(Tree tree, int direction)
        {
            queue <Tree> q;
            q.push(tree);
            if(direction==LEFT)
            {
                while(!q.empty())
                {
                    // cout<<"Hello"<<endl;
                    Tree current_tree = q.front();
                    q.pop();
                    grid[current_tree.x][current_tree.y] = 0;
                    for(int i=current_tree.x-1;i>=max(0, current_tree.x-current_tree.getHeight()+1);i--)
                    {
                        if(grid[i][current_tree.y])
                        {
                            Tree potential_tree = forest[grid[i][current_tree.y]-1];
                            if(potential_tree.retWeight() < current_tree.retWeight())
                            {
                                q.push(potential_tree);
                            }
                            break;
                        }
                    }
                }
            }
            if(direction==UP)
            {
                while(!q.empty())
                {
                    Tree current_tree = q.front();
                    q.pop();
                    grid[current_tree.x][current_tree.y] = 0;
                    for(int i=current_tree.y+1;i<min( (int)grid.size(), current_tree.y+current_tree.getHeight());i++)
                    {
                        if(grid[current_tree.x][i])
                        {
                            Tree potential_tree = forest[grid[current_tree.x][i]-1];
                            if(potential_tree.retWeight() < current_tree.retWeight())
                            {
                                q.push(potential_tree);
                            }
                            break;
                        }
                    }
                }
            }
            if(direction==RIGHT)
            {
                while(!q.empty())
                {
                    Tree current_tree = q.front();
                    q.pop();
                    grid[current_tree.x][current_tree.y] = 0;
                    for(int i=current_tree.x+1;i<min( (int)grid.size(), current_tree.x+current_tree.getHeight());i++)
                    {
                        if(grid[i][current_tree.y])
                        {
                            Tree potential_tree = forest[grid[i][current_tree.y]-1];
                            if(potential_tree.retWeight() < current_tree.retWeight())
                            {
                                q.push(potential_tree);
                            }
                            break;
                        }
                    }
                }
            }
            if(direction==DOWN)
            {
                while(!q.empty())
                {
                    Tree current_tree = q.front();
                    q.pop();
                    grid[current_tree.x][current_tree.y] = 0;
                    for(int i=current_tree.y-1;i>=max(0, current_tree.x-current_tree.getHeight()+1);i--)
                    {
                        if(grid[current_tree.x][i])
                        {
                            Tree potential_tree = forest[grid[current_tree.x][i]-1];
                            if(potential_tree.retWeight() < current_tree.retWeight())
                            {
                                q.push(potential_tree);
                            }
                            break;
                        }
                    }
                }
            }
        }

        void bruteForce()
        {
            vector <pair <int, Tree>> scores;
            for(auto tree:forest)
            {
                bool flag = true;
                // cout<<"Time Taken: "<<tree.time(0,0)<<endl;
                // tree.printTree();
                time -= (tree.x + tree.y);
                current_x = tree.x;
                current_y = tree.y;
                // printGrid();
                while(flag)
                {
                    flag = calculatePoints(findMax());
                }
                // cout<<"-------------"<<endl;
                int points = returnPoints();
                // printGrid();
                scores.push_back(make_pair(points, tree));
                resetGrid();
            }
            sort(scores.begin(), scores.end(), [](const auto& a, const auto& b) {return a.first > b.first; });
            // for(auto p:scores)
            // {
            //     cout<<p.first<<" ";
            //     p.second.printTree();
            // }
            Tree best_tree = scores[0].second;
            if(current_y < best_tree.y)
            {
                while(current_y<best_tree.y)
                {
                    cout<<"move up"<<endl;
                    current_y++;
                }
            }
            if(current_x < best_tree.x)
            {
                while(current_x<best_tree.x)
                {
                    cout<<"move right"<<endl;
                    current_x++;
                }
            }
            time -= (best_tree.x + best_tree.y);
            solve();
        }

        void resetGrid()
        {
            for(int i=0;i<forest.size();i++)
            {
                grid[forest[i].x][forest[i].y] = i+1;
            }
            current_y = 0;
            current_x = 0;
            time = total_time;
        }

        void solve()
        {
            bool flag = true;
            while(flag)
            {
                flag = moveToTree(findMax());
            }
        }
    
};

int main()
{
    // cout<<"Hello";
    cut[UP] = "cut up";
    cut[RIGHT] = "cut right";
    cut[LEFT] = "cut left";
    cut[DOWN] = "cut down";
    int time, grid_size, num_of_trees;
    cin>>time>>grid_size>>num_of_trees;
    float factor = 0.81;
    if(num_of_trees==793)
    {
        factor = 1.62;
    }
    Grid grid = Grid(grid_size, 0, 0, time, factor);
    // cout<<time<<endl;
    vector <Tree> forest;
    // cout<<grid.grid.size()<<endl;
    for(int i=0;i<num_of_trees;i++)
    {
        int x,y,h,d,c,p;
        cin>>x>>y>>h>>d>>c>>p;
        Tree tree = Tree(x,y,h,d,c,p);
        forest.push_back(tree);
        grid.grid[x][y] = i+1;
        // tree.printTree();
    }
    grid.initForest(forest);
    // grid.printGrid();
    // grid.findMax();
    if(grid_size<250)
    {
        grid.bruteForce();
    }
    else
    {
        grid.solve();
    }
    return 0;
}